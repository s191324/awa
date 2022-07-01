# 米游社的Salt
mihoyobbs_Salt = "fd3ykrh7o1j54g581upo1tvpam0dsgtf"
mihoyobbs_Salt_web = "14bmu1mz0yuljprsfgpvjh3ju2ni468r"
mihoyobbs_Salt_web_old = "h8w582wxwgqvahcdkpvdhbh2w9casgfl"
# 米游社的版本
mihoyobbs_Version = "2.7.0"  # Slat和Version相互对应
mihoyobbs_Version_old = "2.3.0"
# 米游社的客户端类型
mihoyobbs_Client_type = "2"  # 1为ios 2为安卓
mihoyobbs_Client_type_web = "5"  # 4为pc web 5为mobile web
# 米游社的分区列表
mihoyobbs_List = [{
    "id": "1",
    "forumId": "1",
    "name": "崩坏3",
    "url": "https://bbs.mihoyo.com/bh3/"
}, {
    "id": "2",
    "forumId": "26",
    "name": "原神",
    "url": "https://bbs.mihoyo.com/ys/"
}, {
    "id": "3",
    "forumId": "30",
    "name": "崩坏2",
    "url": "https://bbs.mihoyo.com/bh2/"
}, {
    "id": "4",
    "forumId": "37",
    "name": "未定事件簿",
    "url": "https://bbs.mihoyo.com/wd/"
}, {
    "id": "5",
    "forumId": "34",
    "name": "大别野",
    "url": "https://bbs.mihoyo.com/dby/"
}, {
    "id": "6",
    "forumId": "52",
    "name": "崩坏：星穹铁道",
    "url": "https://bbs.mihoyo.com/sr/"
}, {
    "id": "8",
    "forumId": "57",
    "name": "绝区零",
    "url": "https://bbs.mihoyo.com/zzz/"
}]

game_id2name = {
    "bh2_cn": "崩坏2",
    "bh3_cn": "崩坏3",
    "nxx_cn": "未定事件簿",
    "hk4e_cn": "原神",
}
# Config Load之后run里面进行列表的选择
mihoyobbs_List_Use = []

# 游戏签到的请求头
headers = {
    'Accept': 'application/json, text/plain, */*',
    'DS': "",
    'Origin': 'https://webstatic.mihoyo.com',
    'x-rpc-app_version': mihoyobbs_Version_old,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Unspecified Device) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 miHoYoBBS/2.3.0',
    'x-rpc-client_type': mihoyobbs_Client_type_web,
    'Referer': '',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'X-Requested-With': 'com.mihoyo.hyperion',
    "Cookie": "",
    'x-rpc-device_id': ""
}

# 通用设置
bbs_Api = "https://bbs-api.mihoyo.com"
web_Api = "https://api-takumi.mihoyo.com"
account_Info_url = web_Api + "/binding/api/getUserGameRolesByCookie?game_biz="

# 米游社的API列表
bbs_Cookie_url = "https://webapi.account.mihoyo.com/Api/cookie_accountinfo_by_loginticket?login_ticket={}"
bbs_Cookie_url2 = web_Api + "/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}"
bbs_Tasks_list = bbs_Api + "/apihub/sapi/getUserMissionsState"  # 获取任务列表
bbs_Sign_url = bbs_Api + "/apihub/sapi/signIn?gids={}"  # post
bbs_List_url = bbs_Api + "/post/api/getForumPostList?forum_id={}&is_good=false&is_hot=false&page_size=20&sort_type=1"
bbs_Detail_url = bbs_Api + "/post/api/getPostFull?post_id={}"
bbs_Share_url = bbs_Api + "/apihub/api/getShareConf?entity_id={}&entity_type=1"
bbs_Like_url = bbs_Api + "/apihub/sapi/upvotePost"  # post json

# 崩坏2自动签到相关的相关设置
honkai2_Act_id = "e202203291431091"
honkai2_checkin_rewards = f'{web_Api}/event/luna/home?lang=zh-cn&act_id={honkai2_Act_id}'
honkai2_Is_signurl = web_Api + "/event/luna/info?lang=zh-cn&act_id={}&region={}&uid={}"
honkai2_Sign_url = web_Api + "/event/luna/sign"

# 崩坏3自动签到相关的设置
honkai3rd_Act_id = "ea20211026151532"
honkai3rd_Is_signurl = web_Api + "/common/eutheniav2/index?act_id={}&region={}&uid={}"
honkai3rd_SignUrl = web_Api + "/common/eutheniav2/sign"

# 原神自动签到相关的设置
genshin_Act_id = "e202009291139501"
genshin_checkin_rewards = f'{web_Api}/event/bbs_sign_reward/home?act_id={genshin_Act_id}'
genshin_Is_signurl = web_Api + "/event/bbs_sign_reward/info?act_id={}&region={}&uid={}"
genshin_Signurl = web_Api + "/event/bbs_sign_reward/sign"
