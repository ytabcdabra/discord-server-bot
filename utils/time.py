from datetime import timedelta

async def convert_time(data: str):
    if data.endswith("d"):
        time = int(data.removesuffix("d"))
        pytime = timedelta(days=time)
        return pytime

    elif data.endswith("h"):
        time = int(data.removesuffix("h"))
        pytime = timedelta(hours=time)
        return pytime

    elif data.endswith("m"):
        time = int(data.removesuffix("m"))
        pytime = timedelta(minutes=time)
        return pytime

    elif data.endswith("s"):
        time = int(data.removesuffix("s"))
        pytime = timedelta(seconds=time)
        return pytime

    else:
        raise ValueError("The time inputted is in an improper format!")