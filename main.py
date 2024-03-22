from linkedin import LinkedInClient
from linkedin_api.clients.restli.response import CreateResponse, GetResponse

import os
from dotenv import load_dotenv

load_dotenv()

# example postId for testing
postId = "7148338267027935233"


def main():
    client = LinkedInClient(os.getenv("ACCESS_TOKEN"))
    
    # user id of the authenticated user for creating new comments
    user: GetResponse = client.get_user_info()
    if(user.status_code == 407):
        print("Failed to get user info")
        return
    userId: str = user['sub']

    comments_response: GetResponse = client.get_comments_on_post(postId)
    for comment in comments_response.entity['elements']:
        commentId: str = comment['id']

        # reply to a comment on a post
        res: CreateResponse = client.reply_to_comment(postId, commentId, userId, "replying to a comment")
        if res.status_code == 201:
            print("Successfully replied to a comment")
            # print(res.entity)
        else:
            print("Failed to reply to a comment")


if __name__ == "__main__":
    main()
    
