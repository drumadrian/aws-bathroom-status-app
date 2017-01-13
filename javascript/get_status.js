'use strict';

var AWS = require("aws-sdk");
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



exports.handler = function(event, context, callback) {
   
    console.log(unique_id);
    docClient.get(params, function(err, data) {
    if (err) {
        console.error("Unable to read item. Error JSON:", JSON.stringify(err, null, 2));
    } else {
        console.log("GetItem succeeded:", JSON.stringify(data, null, 2));
    }
});
    //callback(null, "some success message"){console.log("success");};
};
