from linkedin_api.clients.restli.client import RestliClient


class LinkedInClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.restli_client = RestliClient()

    def get_user_info(self):
        response = self.restli_client.get(
            resource_path="/userinfo",
            access_token=self.access_token
        )
        return response.entity
    
    # gives 403 forbidden
    def get_comments_on_post(self, postId):
        response = self.restli_client.get(
            resource_path="/socialActions/{actionUrn}/comments",
            path_keys={"actionUrn":f"urn:li:activity:{postId}"},
            access_token=self.access_token
        )
        return response.entity

    def comment_on_post(self, postId, userId):
        response = self.restli_client.create(
            resource_path="/socialActions/{actionUrn}/comments",
            path_keys={"actionUrn":f"urn:li:activity:{postId}"},
            entity={
                "actor":f"urn:li:person:{userId}", # authenticated user urn (comment author urn)
                "message":{
                    "text":"hello"
                },
            },
            access_token=self.access_token
        )
        return response.entity
    

    def reply_to_comment(self, postId, commentId, userId):
        response = self.restli_client.create(
            resource_path="/socialActions/{actionUrn}/comments",
            path_keys={"actionUrn":f"urn:li:comment:(urn:li:activity:{postId},{commentId})"},
            entity={
                "actor":f"urn:li:person:{userId}",
                "message":{
                    "text":"replying to u"
                },
                "parentComment": f"urn:li:comment:(urn:li:activity:{postId},{commentId})",
            },
            access_token=self.access_token
        )
        return response.entity
