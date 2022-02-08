import { createRouter, createWebHistory } from 'vue-router';
import store from '../store';
import Home from '../views/Home.vue';
import Cookies from "js-cookie";

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: "Welcome | Career Guidance",
      transition: 1,
      transitionName: "",
    },
    beforeEnter: (to) => {
      document.title = to.meta.title;
    },
  },
  {
    path: '/:staffId',
    name: 'staff',
    redirect: {name: 'dashboard'},
    component: () => import(/* webpackChunkName: "staff" */ '../views/Staff.vue'),
    props: true,
    meta: {
      requiresAth: true,
      title: "Dashboard | Career Guidance",
      transition: 3,
      transitionName: "",
    },
    beforeEnter: (to) => {
      if (to.meta.requiresAth && !Cookies.get("authToken")) {
        return {name: 'signin'}
      }
      else {
        document.title = to.meta.title;
        return true
      }
    },
    children: [ // nested routes
      {
        path: "dashboard",
        name: "dashboard",
        component: () => import(/* webpackChunkName: "dashboard" */ '../components/AppStaffDashBoard.vue'),
      },
      {
        path: "myschedules",
        name: "myschedules",
        component: () => import(/* webpackChunkName: "schedules" */ '../components/AppStaffSchedule.vue'),
        meta: {title: "Schedules | Career Guidance"},
        beforeEnter: (to) => {document.title = to.meta.title;}
      },
      {
        path: "mystudents",
        name: "mystudents",
        component: () => import(/* webpackChunkName: "students" */ '../components/AppStudent.vue'),
        meta: {title: "Students | Career Guidance"},
        beforeEnter: (to) => {document.title = to.meta.title;}
      },
      {
        path: "mystudents/:regNo",
        name: "details",
        props: true,
        redirect: {name: 'studentdata'},
        component: () => import(/* webpackChunkName: "details" */ '../components/AppStudentDetail.vue'),
        children: [ // nested routes
          {
            path: "data",
            name: "studentdata",
            component: () => import(/* webpackChunkName: "studentdata" */ '../components/AppStudentData.vue'),
          },
          {
            path: "observation",
            name: "studentobservation",
            component: () => import(/* webpackChunkName: "studentobservation" */ '../components/AppStudentObservation.vue'),
          },
        ]
      },
    ]
  },
  {
    path: "/signin",
    name: "signin",
    component: () => import(/* webpackChunkName: "signout" */ '../views/Signin.vue'),
    meta: {title: "Sign in | Career Guidance", transition: 2, transitionName: ""},
    beforeEnter: (to) => {
      if (Cookies.get("authToken")) {
        return {name: "staff", params: {staffId: store.state.staffData.staff_id}}
      }
      else {
        document.title = to.meta.title;
        return true;
      }
    }
  },
  {
    path: "/:pathMatch(.*)*",
    name: "notfound",
    component: () => import(/* webpackChunkName: "notfound" */ '../views/NotFound.vue'),
    meta: {transition: 10},
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.afterEach((to, from) => {
  // set the transition name of the incoming route, base on the
  // the direction of the route
  to.meta.transitionName = to.meta.transition > from.meta.transition ? "slide-left":"slide-right";
})

export default router
