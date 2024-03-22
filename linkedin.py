from linkedin_api.clients.restli.client import RestliClient
from linkedin_api.clients.restli.response import CreateResponse, GetResponse


"""
LinkedInClient class for interacting with LinkedIn API
"""
class LinkedInClient:
    restli_client: RestliClient = RestliClient()

    def __init__(self, access_token):
        self.access_token: str = access_token

    def get_user_info(self) -> GetResponse:
        return self.restli_client.get(
            resource_path="/userinfo",
            access_token=self.access_token
        )
    
    # works for "r_organization_social" oauth scope access tokens only
    # restricted access to select devs with "r_member_social" scope
    # need access to Advertising API endpoints; verify company page
    def get_comments_on_post(self, postId) -> GetResponse:
        return self.restli_client.get_all(
            resource_path="/socialActions/{actionUrn}/comments",
            path_keys={"actionUrn":f"urn:li:activity:{postId}"},
            access_token=self.access_token
        )

    def comment_on_post(self, postId, userId, message) -> CreateResponse:
        return self.restli_client.create(
            resource_path="/socialActions/{actionUrn}/comments",
            path_keys={"actionUrn":f"urn:li:activity:{postId}"},
            entity={
                "actor":f"urn:li:person:{userId}", # replace person with organization to comment as company
                "message":{
                    "text":message
                },
            },
            access_token=self.access_token
        )
    

    def reply_to_comment(self, postId, commentId, userId, message) -> CreateResponse:
        return self.restli_client.create(
            resource_path="/socialActions/{actionUrn}/comments",
            path_keys={"actionUrn":f"urn:li:comment:(urn:li:activity:{postId},{commentId})"},
            entity={
                "actor":f"urn:li:person:{userId}",
                "message":{
                    "text":message
                },
                "parentComment": f"urn:li:comment:(urn:li:activity:{postId},{commentId})",
            },
            access_token=self.access_token
        )
