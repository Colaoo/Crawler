from .common import common_request

def request_search(keyword: str, cookie: str, offset: int = 0, limit: int = 10) -> tuple[dict, bool]:
    """
    请求抖音获取搜索信息
    """
    params = {"keyword": keyword, "search_channel": 'aweme_general', "search_source": 'normal_search',
              "query_correct_type": '1', "is_filter_search": '0', 'offset': offset, 'count': limit}
    headers = {"cookie": cookie}
    return common_request('/aweme/v1/web/general/search/single/', params, headers)
