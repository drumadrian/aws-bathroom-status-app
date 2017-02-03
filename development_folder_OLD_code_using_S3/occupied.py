def lambda_handler(event, context):



        import boto3
        import botocore


        #Substatus = ""


        print "START UPDATE: Change to OCCUPIED"
        print ""
        print ""


        #Create and write text file to temp directory
        text_file = open("/tmp/bathroom1_status.txt", "w")
        #text_file.write("<html><head><title>bathroom1</title></head><body>occupied</body></html>")
        text_file.write("occupied")
        text_file.close()


        ##Check to see if file exists
        s3 = boto3.resource('s3')
        exists = False

        try:
            s3.Object('room4562', 'bathroom1_status.txt').load()
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                exists = False
            else:
                raise e
        else:
            exists = True

        print(exists)

        #Delete old file in S3 if it exists
        if exists == True:
            
            object = s3.Object('room4562','bathroom1_status.txt')
            object.delete()
            print "Object Deleted"
            print ""
            print ""



        #Put new file in S3
        s3.Bucket('room4562').upload_file('/tmp/bathroom1_status.txt', 'bathroom1_status.txt')

        print "Object Uploaded"
        print ""
        print ""


        print "END UPDATE: Changed to OCCUPIED"
        print ""
        print ""