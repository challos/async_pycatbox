import aiohttp


class Uploader:
    def __init__(self, token: str = ""):
        self.token = token
        self.apiUrl = "https://catbox.moe/user/api.php"

    async def upload(self, file_type: str = None, file_raw: bytes = None):
        data = aiohttp.FormData()
        data.add_field("reqtype", "fileupload")
        data.add_field("userhash", self.token)
        data.add_field("fileToUpload", file_raw, filename="file.{}".format(file_type))
        async with aiohttp.ClientSession() as session:

            async def post(data):
                async with session.post(self.apiUrl, data=data) as response:
                    resp = response
                    text = await resp.text()
                    return text 

            return await post(data)
