from rknn.api import RKNN

if __name__ == "__main__":
    rknn = RKNN()

    # 使用load_rknn接口导入RKNN模型
    rknn.load_rknn(path="../model/yolo113588.rknn")

    # 使用init_runtime接口初始化运行环境
    rknn.init_runtime(
        # target = None,
        target="rk3588",
        perf_debug = True,          # 表示是否开启性能评估的Debug模式
        eval_mem = False,            # 表示是否是内存评估
    )

    # 使用eval_perf接口进行性能评估
    rknn.eval_perf(
        inputs = ["space_shuttle_224.jpg"],    # 表示要测试的图片
        data_format=None,                      # 表示要推理的数据模式
        is_print = True,                       # 表示使能打印性能信息

    )

    rknn.release()
