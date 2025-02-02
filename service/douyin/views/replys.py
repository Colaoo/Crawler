from flask import request
from utils.error_code import ErrorCode
from utils.reply import reply
from ..models import accounts
from lib.logger import logger
from ..logic import request_reply
import random

def replys():
    """
    获取视频评论回复
    """
    video_id = request.args.get('video_id', '')
    comment_id = request.args.get('comment_id', '')
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', 20)
    _accounts = accounts.load()
    random.shuffle(_accounts)
    for account in _accounts:
        res, expired = request_reply(video_id, comment_id, account.get('cookie', ''), offset, limit)
        if expired:
            accounts.expire(account.get('id', ''))
        if res == {} or expired:
            continue
        logger.info(f'get reply success, video_id: {video_id}, comment_id: {comment_id}, offset: {offset}, limit: {limit}, res: {res}')
        return reply(ErrorCode.OK, '成功' , res)
    logger.warning(f'get reply failed, video_id: {video_id}, comment_id: {comment_id}, offset: {offset}, limit: {limit}')
    return reply(ErrorCode.INTERNAL_ERROR, '内部错误请重试')