#!/bin/bash

echo "**** Creating first user (A) ****"
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Test User","email":"abc@test.com", "password": "123456"}' http://127.0.0.1:5000/puppies/api/v1.0/users

echo

echo "**** Creating second user (B) ****"
curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abcd@test.com", "password": "123456"}' http://127.0.0.1:5000/puppies/api/v1.0/users

echo

echo " **** Signing in as user A ****"
curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abc@test.com", "password": "123456"}' http://127.0.0.1:5000/puppies/api/v1.0/signin

echo "Please copy the session cookie from the header [i.e. session=[COPY THIS PART FROM HEADER]; ...]. After you have copied it, please provide the session cookie and press ENTER"

read SESSION_COOKIE

echo

echo "**** Getting details of user A ****"
curl -i -H "Content-Type: application/json" -X GET --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/users/1

echo

echo "**** Getting details of user B ****"
curl -i -H "Content-Type: application/json" -X GET --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/users/2

echo

echo "**** Creating a post ****"
echo "Please provide a path to an image that needs to be uploaded [Press ENTER if you do not want a file to be uploaded]"

read FILE_PATH

if [ -f ${FILE_PATH} ]; then
    curl -X POST -F content=Testcontent -F file=@${FILE_PATH} --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/posts
else
    curl -X POST -F content=Testcontent --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/posts
fi

echo

echo "**** Creating one more post ****"
    curl -X POST -F content=Testcontent2 --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/posts

echo

echo "**** Getting post info of all posts ****"
curl -i -H "Content-Type: application/json" -X GET --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/posts

echo

echo "**** Liking the first post ****"
curl -i -H "Content-Type: application/json" -X PUT --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/posts/1/like

echo

echo "**** Getting post info of first post ****"
curl -i -H "Content-Type: application/json" -X GET --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/posts/1

echo

echo "**** Getting all posts created by user A ****"
curl -i -H "Content-Type: application/json" -X GET --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/users/1/posts

echo

echo "**** Getting all posts liked by user A ****"
curl -i -H "Content-Type: application/json" -X GET --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/users/1/posts/likes

echo "**** Signing out ****"
curl -i -H "Content-Type: application/json" -X GET --cookie "session=${SESSION_COOKIE}" http://127.0.0.1:5000/puppies/api/v1.0/signout

