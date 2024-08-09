import { createRouter, createWebHistory } from "vue-router"
import Threads from "../views/Threads.vue"
import UserAccount from "../views/UserAccount.vue"

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/threads",
      name: "thread",
      component: Threads,
    },
    {
      path: "/user/userId",
      name: "user",
      component: UserAccount,
    },
  ],
})

export default router
