<template>
    <div>
        <el-table
            :data="tableData"
            ref="table"
            header-row-class-name="tableHead"
            header-cell-class-name="tableHeadCell"
            cell-class-name="tableCell"
            max-height="250">
            <el-table-column prop="" type="index" width="120" :label="$t('m.common.index')" ></el-table-column>
            <el-table-column prop="networkAccess" :label="$t('m.ip.rollsiteNetworkAccess')"   show-overflow-tooltip></el-table-column>
            <el-table-column prop="" :label="$t('m.ip.routerNetworkAccess')" show-overflow-tooltip>
                <template slot-scope="scope">
                    <span @click="toShowSiteNet(scope.row.partyDos)" style="color:#217AD9;cursor: pointer;">{{scope.row.partyDos && scope.row.partyDos.length}}</span>
                </template>
            </el-table-column>
            <el-table-column prop="status" :label="$t('m.ip.status')">
                <template slot-scope="scope">
                    {{$t('m.common.'+scope.row.status)}}
                </template>
            </el-table-column>
            <el-table-column prop="updateTime" :label="$t('m.common.updateTime')"  show-overflow-tooltip>
                <template slot-scope="scope">
                    <span>{{scope.row.updateTime | dateFormat}}</span>
                </template>
            </el-table-column>
            <el-table-column prop=""  :label="$t('m.common.action')" align="center" show-overflow-tooltip>
                <template slot-scope="scope">
                    <el-button v-if="scope.row.status==='unpublished'" @click="clickPublish(scope.row.rollSiteId)" type="text">
                        {{$t('m.common.publish')}}
                    </el-button>
                    <el-button @click="rollsiteEdit(scope.row)" type="text">
                        <i class="el-icon-edit edit" ></i>
                    </el-button>
                    <el-button type="text" @click="toDeleteRollsite(scope.row)">
                        <i class="el-icon-delete-solid delete" ></i>
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <div class="collapse-pagination">
            <el-pagination
                background
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page.sync="currentPage"
                :page-size="data.pageSize"
                layout="total, prev, pager, next, jumper"
                :total="total"
            ></el-pagination>
        </div>
        <!-- 显示Site Network -->
        <el-dialog :visible.sync="showSiteNet" class="show-site-dialog" width="780px">
            <div class="site-net-title">
                {{$t('m.ip.routerInfo')}}
            </div>
            <div class="site-net-table">
                <el-table
                    :data="siteNetData"
                    max-height="250" >
                    <el-table-column type="index" :label="$t('m.common.index')" width="80" >
                    </el-table-column>
                    <el-table-column prop="partyId" :label="$t('m.common.partyID')"  width="90">
                    </el-table-column>
                    <el-table-column  prop="networkAccess" :label="$t('m.ip.routerNetworkAccess')" width="165" show-overflow-tooltip>
                    </el-table-column>
                    <el-table-column  prop="secureStatus" :label="$t('m.ip.isSecure')" width="80">
                        <template slot-scope="scope">
                            <span>{{scope.row.secureStatus===1? $t('m.common.true') : $t('m.common.false') }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column  prop="pollingStatus" :label="$t('m.ip.isPolling')" >
                        <template slot-scope="scope">
                            <span>{{scope.row.pollingStatus===1? $t('m.common.true') : $t('m.common.false') }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column  prop="updateTime" :label="$t('m.common.updateTime')" width="170" show-overflow-tooltip>
                        <template slot-scope="scope">
                            <span>{{scope.row.validTime | dateFormat}}</span>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </el-dialog>
         <!-- 删除 -->
        <el-dialog :visible.sync="deletedialog" class="access-delete-dialog" width="700px">
            <div class="line-text-one">{{$t('m.ip.sureWantDeleteRollsite')}}</div>
            <div class="dialog-footer">
                <el-button class="ok-btn" type="primary" @click="toDelet">{{$t('m.common.sure')}}</el-button>
                <el-button class="ok-btn" type="info" @click="deletedialog = false">{{$t('m.common.cancel')}}</el-button>
            </div>
        </el-dialog>
          <!-- 删除 -->
        <el-dialog :visible.sync="publishdialog" class="sure-exchange-dialog" width="700px">
            <div class="line-text-one">{{$t('m.ip.SureWantPublishRollsite')}} </div>
            <div class="line-text-two">{{$t('m.ip.updateToServer')}}</div>
            <div class="dialog-footer">
                <el-button class="ok-btn" type="primary" @click="toClickPublish">{{$t('m.common.sure')}}</el-button>
                <el-button class="ok-btn" type="info" @click="publishdialog = false">{{$t('m.common.cancel')}}</el-button>
            </div>
        </el-dialog>

        <ipaddrollsite ref="ipaddrollsite"/>
    </div>
</template>

<script>
import { getRollsiteList, toPublish, deleteRollsite } from '@/api/federated'
import moment from 'moment'
import ipaddrollsite from './ipaddrollsite'

export default {
    name: 'Ip',
    components: { ipaddrollsite },
    // filters: {
    //     dateFormat(value) {
    //         return moment(value).format('YYYY-MM-DD HH:mm:ss')
    //     }
    // },
    props: {
        exchangeId: {
            type: Number,
            default: function() {
                return 0
            }
        }
    },
    data() {
        return {
            activeName: [], // 折叠版激活
            deletedialog: false, // 删除框
            editdialog: false,
            showSiteNet: false,
            publishdialog: false,
            siteNetType: 'add',
            siteNetIndex: 0,
            currentPage: 1, // 当前页
            tableData: [ ], // 表格数据
            siteNetData: [],
            tempStatusStr: '{}',
            data: {
                pageNum: 1,
                pageSize: 20
            },
            total: 0,
            deleteRollSiteId: '',
            rollSiteId: ''
        }
    },
    created() {
    },
    mounted() {

    },
    methods: {
        togetRollsiteList() {
            this.data.exchangeId = this.exchangeId
            getRollsiteList(this.data).then(res => {
                this.tableData = res.data.list
                // this.tableData.length > 0 && this.tableData.map(item => item.status = this.$t('m.common.this.tableData'))
                this.total = res.data && res.data.totalRecord
            })
        },
        initList() {
            this.$parent.$parent.$parent.initList()
        },
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`)
        },
        handleCurrentChange(val) {
            this.data.pageNum = val
            this.togetRollsiteList()
        },
        // 删除弹框
        toDeleteRollsite(row) {
            this.deleteRollSiteId = row.rollSiteId
            this.deletedialog = true
        },
        // 确认删除
        toDelet() {
            let data = {
                rollSiteId: this.deleteRollSiteId
            }
            deleteRollsite(data).then(res => {
                this.deletedialog = false
                this.initList()
            })
        },
        // 编辑rollsite
        rollsiteEdit(row) {
            this.$refs['ipaddrollsite'].exchangeData.networkAccess = row.networkAccess
            this.$refs['ipaddrollsite'].editdialog = true
            this.$refs['ipaddrollsite'].rollsiteType = 'edit'
            setTimeout(() => {
                this.$refs['ipaddrollsite'].toAcquire()
            }, 300)
        },
        // 显示siteNet列表弹框
        toShowSiteNet(row) {
            this.showSiteNet = true
            this.siteNetData = [ ...row ]
        },
        clickPublish(rollSiteId) {
            this.publishdialog = true
            this.rollSiteId = rollSiteId
        },
        // 点击publish
        toClickPublish() {
            let data = {
                rollSiteId: this.rollSiteId
            }
            toPublish(data).then(res => {
                this.publishdialog = false
                // this.togetRollsiteList()
                this.initList()
            })
        }

    }
}
</script>

<style rel="stylesheet/scss" lang="scss">
@import 'src/styles/ip.scss';
.site-net-table{
    .el-table_3_column_20{
        .cell{
            width: 150px
        }
    }
}
</style>
