from linkedin import LinkedInClient
import os
from dotenv import load_dotenv

load_dotenv()

# example post and comment ids for testing
postId = "7148338267027935233"
commentId = "7176868771452641280"


def main():
    client = LinkedInClient(os.getenv("ACCESS_TOKEN"))
    # user id of the authenticated user for creating new comments
    userId = client.get_user_info()['sub']
    # reply to a comment on a post
    print(client.reply_to_comment(postId, commentId, userId))


if __name__ == "__main__":
    main()
    
