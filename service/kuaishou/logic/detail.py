from .common import common_request, load_graphql_queries, GraphqlQuery


def request_detail(id: str, cookie: str) -> tuple[dict, bool]:
    """
    请求快手获取视频信息
    """
    data = {
        "operationName": "visionVideoDetail",
        "variables": {
            "photoId": id,
            "page": "search"
        },
        "query": load_graphql_queries(GraphqlQuery.DETAIL)
    }
    headers = {"Cookie": cookie}
    return common_request(data, headers)
