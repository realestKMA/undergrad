<template>
    <div class="relative w-full h-screen min-h-full flex bg-slate-100">

        <!-- start of left nav -->
        <div :class="nav ? 'opacity-100':'-translate-x-full opacity-0'" class="absolute top-0 left-0 w-full h-screen min-h-[44rem] bg-transparent overflow-hidden backdrop-blur-sm transition-all duration-200 lg:contents z-50 lg:fixed lg:backdrop-blur-none">
            <div class="relative w-10/12 h-screen min-h-[44rem] flex flex-col items-center space-y-20 pb-10 bg-slate-100 lg:w-1/5">
                <div class="absolute top-5 right-5 lg:hidden">
                    <AppCloseButton @click.prevent="actionUpdateNav({state: false})" />
                </div>
                <AppTextLogo :position="'center'" :text="'small'" />
                <AppLeftNavLinks />
            </div>
        </div>
        <!-- end of side nav -->

        <!-- start of main view -->
        <div class="w-full h-full bg-transparent p-0 overflow-hidden xl:py-4">
            
            <div class="w-full h-full bg-white p-4 overflow-y-auto shadow-inner xl:rounded-l-2xl xl:px-8 xl:py-4">
                <div class="flex justify-between items-center top-10 right-16 z-20 xl:fixed">
                    <AppLeftNavButton />
                    <AppStudentId :studentData="studentData" />
                </div>

                <router-view v-slot="{Component}">
                    <transition name="slide">
                        <keep-alive>
                            <component :is='Component' />
                        </keep-alive>
                    </transition>
                </router-view>
            </div>

        </div>
        <!-- end of main view -->

        <teleport to='body'>
            <div v-if="signout" class="w-screen h-screen absolute top-0 left-0 flex justify-center items-center bg-slate-500/50 backdrop-blur z-50">
                <AppNotificationModal :type="'signout'" :title="'Sign out'" :text="'Are you sure you want to sign out?'">
                        <AppButton @click.prevent="actionUpdateSignout({state: false}), actionUpdateNav({state: false})" :name="'Cancle'" :type="'plain'" />
                        <AppButton @click.prevent="signOut()" :name="'Sign out'" />
                </AppNotificationModal>
            </div>
        </teleport>

    </div>
</template>

<script>
import {mapState, mapActions} from "vuex";
import AppButton from "@/components/AppButton.vue";
import AppStudentId from "@/components/AppStudentId.vue";
import AppTextLogo from "@/components/AppTextLogo.vue";
import AppCloseButton from "@/components/AppCloseButton.vue";
import AppLeftNavLinks from "@/components/AppLeftNavLinks.vue";
import AppLeftNavButton from "@/components/AppLeftNavButton.vue";
import AppNotificationModal from "@/components/AppNotificationModal.vue";

export default {
    name: "Student",
    props: {
        department: {type: String, required: true},
        level: {type: String, required: true},
        regNo: {type: String, required: true},
    },
    components: {
        AppStudentId, AppTextLogo, AppCloseButton, AppLeftNavLinks,
        AppLeftNavButton, AppNotificationModal, AppButton
    },
    computed: {
        ...mapState({
            nav: state => state.nav,
            signout: state => state.signout,
            studentData: state => state.studentData,
        }),
    },
    methods: {
        ...mapActions([
            "actionUpdateNav",
            "actionUpdateSignout",
            "actionSignout",
        ]),
        async signOut() {
            this.actionUpdateNav({state: false});
            await this.$router.push({name: "home"});
            this.actionSignout({state: false});
        }
    },
}
</script>