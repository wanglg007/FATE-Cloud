<template>
<div>
<img src="@/assets/welcomepage.svg" />
  <div class="register">
        <div class="title">{{$t('m.sitemanage.register')}}</div>
            <div class="organization">
            <div class="name-tip">
                <span>{{$t('m.sitemanage.pleaseEnterRegistration')}}</span>
            </div>
            <el-form ref="inputform" :model="inputform" :rules="rules" @submit.native.prevent >
                <el-form-item :class="{ name:true,'name-warn': warnActive }" prop="inputUrl">
                    <el-input :class="{ 'active': inputClass }" placeholder="" clearable v-model="inputform.input"></el-input>
                    <div class="warn-text">
                        <span v-show='warnActive'>{{$t('m.sitemanage.registrationInvalid')}}</span>
                    </div>
                </el-form-item>
            </el-form>
            </div>
            <div class="btn">
                <el-button class="OK-btn" :type="type" :disabled="disabledbtn" @click="okAction">{{$t('m.common.OK')}}</el-button>
                <el-button class="Cancel-btn" type="info"  @click="cancelAction">{{$t('m.common.cancel')}}</el-button>
            </div>
    </div>
  </div>
</template>

<script>
import { checkUrl } from '@/api/welcomepage'
import { decode64, utf8to16 } from '@/utils/base64'
export default {
    name: 'home',
    components: {},
    data() {
        return {
            inputClass: false, // 是否显示输入框样式
            warnActive: false, // 显示警告样式
            disabledbtn: true, // 按钮可点击
            type: 'info',
            inputform: { inputUrl: '' },
            inputUrl: '', // 输入框URL
            rules: {
                inputUrl: [
                    { type: 'url', message: ' ', trigger: 'change' }
                ]
            }
        }
    },
    watch: {
        'inputform.input': {
            handler: function(val) {
                // this.showBtn()
                if (val) {
                    this.inputClass = true
                    let url = this.inputform.input.split('\\n').join('')
                    console.log(url, 'url-watch')
                    this.inputform.inputUrl = url ? utf8to16(decode64(url)).split('?st')[0] : ''
                    console.log(this.inputform.inputUrl, 'this.inputform.inputUrl')
                    this.$refs['inputform'].validateField('inputUrl', valid => {
                        if (valid) {
                            this.warnActive = true
                        } else {
                            this.disabledbtn = false
                            this.type = 'primary'
                        }
                    })
                } else {
                    this.disabledbtn = true
                    this.type = 'info'
                    this.warnActive = false
                    this.inputClass = false
                }
            },
            immediate: true
        }
    },
    computed: {},
    mounted() {

    },
    methods: {

        okAction() {
            let urlStr = this.inputform.input.split('\\n').join('')
            let Url = utf8to16(decode64(urlStr))
            let newStr = Url.split('st=')[1].replace(new RegExp('\\\\', 'g'), '')
            this.inputform.input = this.inputform.input.replace(/\\n/g, '\n')
            // 判断URL后面是否是json
            try {
                let data = {}
                var obj = { ...JSON.parse(newStr) }
                data.appKey = obj.secretInfo.key
                data.appSecret = obj.secretInfo.secret
                data.federatedUrl = `${Url.split('//')[0]}//${Url.split('//')[1].split('/')[0]}`
                data.registrationLink = this.inputform.input
                data.federatedOrganization = obj.federatedOrganization
                data.id = obj.id
                data.institutions = obj.institutions
                data.networkAccessEntrances = obj.networkAccessEntrances
                data.networkAccessEntrances = obj.networkAccessExits
                data.partyId = obj.partyId
                data.role = obj.role
                data.siteName = obj.siteName
                checkUrl(data).then(res => {
                    if (res.code === 0) {
                        this.$router.push({
                            name: 'activate',
                            query: { registerUrl: this.inputform.input }
                        })
                    }
                }).catch(res => {
                    this.warnActive = true
                })
            } catch (err) {
                this.warnActive = true
            }
        },
        cancelAction() {
            this.$router.go(-1)
        }
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" >
@import 'src/styles/register.scss';
</style>
