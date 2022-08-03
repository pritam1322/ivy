# global
import ivy


def add(input, other, *, alpha=1, out=None):
    return ivy.add(input, other * alpha, out=out)


add.unsupported_dtypes = ("float16",)


def tan(input, *, out=None):
    return ivy.tan(input, out=out)


tan.unsupported_dtypes = ("float16",)


def cos(input, *, out=None):
    return ivy.cos(input, out=out)


cos.unsupported_dtypes = ("float16",)


def sin(input, *, out=None):
    return ivy.sin(input, out=out)


sin.unsupported_dtypes= ("float16",)


def acos(input, *, out=None):
    return ivy.acos(input, out=out)


acos.unsupported_dtypes= ("float16",)


def abs(input, *, out=None):
    return ivy.abs(input, out=out)
