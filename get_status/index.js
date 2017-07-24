'use strict';

exports.handler = (event, context, callback) => {

var AWS = require("aws-sdk");
// var JSON = require("JSON");
AWS.config.update({
  region: "us-west-2",
  endpoint: "dynamodb.us-west-2.amazonaws.com"
});


var docClient = new AWS.DynamoDB.DocumentClient()

var table = "study-guru-bathrooms";
var gender = "F";
var stall = 10;
var bathroom = 2;
// var unique_id = gender+stall+bathroom;

var unique_id = event.unique_id;
var unique_id2 = event["unique-id"];

console.log("Printing unique_id");
console.log(event.unique_id);


//console.log("unique_id is an instance of");
//console.log(instanceof event);


// console.log("Printing JSON parsed unique_id");
// console.log(JSON.parse(event));



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
//        console.log("GetItem succeeded:", JSON.stringify(data, null, 2));
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

    //Old way return 
    // context.succeed(data);

    // New way (Node.js runtime v4.3).
    context.callbackWaitsForEmptyEventLoop = false; 
    // callback(null, 'Success message');  
    callback(null, data);  


});
    // callback(null, "some success message"){console.log("success");};
    // callback(null, data);//{console.log("success");};

};


// exports.handler();