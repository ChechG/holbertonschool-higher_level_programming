#!/bin/bash
# causes server to respond with a message containing You got me!.
curl -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
