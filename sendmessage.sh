 #!/bin/sh

MESSAGE=${1:-'I love Bob Dole!'}

curl -d '{"text" : "'"$MESSAGE"'", "bot_id" : "e18f0a0d058420de66f2e2a387"}' https://api.groupme.com/v3/bots/post

