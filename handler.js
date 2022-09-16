'use strict';

module.exports.record_cause = async (event) => {
  console.log(event);
  
  if (event['currentIntent']['name'] == "CauseIntent") {
    console.log(event['currentIntent']['slots']);
  }
  return {
    "dialogAction" : {
      "type": "Close",
      "fullfillmentState": "Fulfiled"
    }
  };
};
