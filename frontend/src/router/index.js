import {
    createRouter,
    createWebHistory
} from "vue-router";

import Dashboard from "../views/Dashboard.vue";
import Workloads from "../views/Workloads.vue";
import History from "../views/History.vue";
import Compare from "../views/Compare.vue";
import Report from "../views/Report.vue";

const routes = [
    {
        path: "/",
        component: Dashboard
    },
    {
        path: "/workloads",
        component: Workloads
    },
    {
        path: "/history/:workload",
        component: History
    },
    {
        path: "/compare/:workload",
        component: Compare
    },
    {
        path: "/report/:workload",
        component: Report
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;