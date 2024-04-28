#!/bin/bash
#GET request to the URL, and displays the body of the response
#A header variable X-School-User-Id must be sent with the value 98
curl $1 -X GET -H X-School-User-Id: 98
