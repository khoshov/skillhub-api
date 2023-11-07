from asgiref.sync import sync_to_async


@sync_to_async
def get_descendants(qs):
    return qs.get_descendants(include_self=True)
