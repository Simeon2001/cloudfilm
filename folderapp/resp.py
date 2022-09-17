from rest_framework import status
from rest_framework.response import Response


def created(msg):
    return Response(
        {"status": True, "message": msg},
        status=status.HTTP_201_CREATED,
    )


def accepted(msg):
    return Response(
        {"status": True, "message": msg},
        status=status.HTTP_202_ACCEPTED,
    )


def it_ok(msg):
    return Response(
        {"status": True, "message": msg},
        status=status.HTTP_200_OK,
    )


def forbidden(msg):
    return Response(
        {"status": True, "message": msg},
        status.HTTP_403_FORBIDDEN,
    )


def not_found(msg):
    return Response(
        {"status": False, "message": msg},
        status=status.HTTP_404_NOT_FOUND,
    )


def media_error(msg):
    return Response(
        {"status": False, "message": msg},
        status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    )


def not_yours(msg):
    return Response(
        {"status": False, "message": msg},
        status=status.HTTP_401_UNAUTHORIZED,
    )


def bad(msg):
    return Response(
        {"status": False, "message": msg},
        status=status.HTTP_400_BAD_REQUEST,
    )
