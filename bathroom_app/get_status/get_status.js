'use strict';
exports.handler = (event, context, callback) => {

var AWS = require("aws-sdk");
AWS.config.update({
  region: "us-west-2",
  endpoint: "dynamodb.us-west-2.amazonaws.com"
});


var docClient = new AWS.DynamoDB.DocumentClient()

var table = "study-guru-bathrooms";
var gender = "F";
var stall = 10;
var bathroom = 2;
var unique_id = gender+stall+bathroom;

var params = {
    TableName: table,
    Key:{
        "unique_id": unique_id     
    }
};
    console.log(unique_id);
    docClient.get(params, function(err, data) {
    if (err) {
        console.error("Unable to read item. Error JSON:", JSON.stringify(err, null, 2));
    } else {
       //console.log("GetItem succeeded:", JSON.stringify(data, null, 2));
        console.log("GetItem succeeded:", JSON.stringify(data, data, 2));
    }
    
    //build the repsonse object for API Gateway 
    var response = {
        statusCode: 200,
        headers: {
            "x-custom-header" : "my custom header value"
        },
        body: JSON.stringify(data)
    };
    console.log("response: " + JSON.stringify(response))


    //Reference:    http://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-using-old-runtime.html#transition-to-new-nodejs-runtime
    //Old way return 
    // context.succeed(data);

    // New way (Node.js runtime v4.3).
    context.callbackWaitsForEmptyEventLoop = true; 
    // callback(null, 'Success message');  
    callback(null, data);  


});
    // callback(null, "some success message"){console.log("success");};
    // callback(null, data);//{console.log("success");};

};


// exports.handler();