# 标本与检测板合成输入

这是新系统起点，仅含输入，没有现成数量台账、检测仓或目标答案。所有标本和规则均为本题虚构，数值单位为微升/任意响应单位。

`case.json`的initial_receipts给已核接收的root_id、sample_id、volume_ul；其actions是要求候选处理的有序动作示例。占用和消耗都按容器的自身剩余量扣减；分出给子容器的量不再属于父容器。root身份沿分装父链追溯，板文件不提供root的接收、撤销或数量事实。

`plate.csv`按CSV表头读取，空字段表示对该kind不适用。standard的concentration、qc的known_concentration/tolerance、sample的aliquot_id/run_id/dilution按题面定义。plate_id统一为P1；well_id标识原始孔，不是标准浓度或样本身份。样本两孔均为同一个技术重复组，不代表两次独立复测。响应是有限十进制，不能经二进制浮点再宣称精确。

输入可增加为题面界定的合法范围，不仅支持这组固定数据。请自行提供持久化目录、API或CLI及演示入口；内部作者探针与审核文件不属于候选材料。
