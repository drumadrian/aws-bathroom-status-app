'use strict';

console.log('Loading function');

const doc = require('dynamodb-doc');

const dynamo = new doc.DynamoDB();

var AWS = require("aws-sdk");



// exports.handler = function(event, context, callback) {



AWS.config.update({
  region: "us-west-2",
  endpoint: "dynamodb.us-west-2.amazonaws.com"
});



var docClient = new AWS.DynamoDB.DocumentClient()


var table = "study-guru-bathrooms";

var bathroom = 2;
var stall = 10;
var gender = "F";
var unique_id = 'F102'

var params = {
    TableName: table,
    Key:{
        "unique_id": unique_id
    }
};
// var params = {
//     TableName: table,
//     Key:{
//         "bathroom": bathroom,
//         "stall": stall,
//         "gender": gender
//     }
// };




//};    //End of main AWS Lambda 


// exports.handler("","","");







