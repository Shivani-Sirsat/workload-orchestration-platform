<template>

  <div class="report">

    <h1>Benchmark Report</h1>

    <p class="subtitle">
      Latest benchmark execution report.
    </p>

    <div
      v-if="!report"
      class="empty-state"
    >
      No report data available.
    </div>

    <div
      v-else
      class="report-card"
    >

      <h2>
        {{ workload }}
      </h2>

      <table>

        <thead>
          <tr>
            <th>KPI</th>
            <th>Value</th>
          </tr>
        </thead>

        <tbody>

          <tr
            v-for="(value, key) in report"
            :key="key"
          >
            <td>{{ key }}</td>
            <td>{{ value }}</td>
          </tr>

        </tbody>

      </table>

    </div>

  </div>

</template>

<script setup>

import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import api from "../services/api";

const route = useRoute();

const report = ref(null);

const workload =
    route.params.workload;

onMounted(async () => {

    try {

        const response =
            await api.get(
                `/report/${workload}`
            );

        report.value =
            response.data;

    } catch (error) {

        console.error(
            "Failed to load report",
            error
        );

    }

});

</script>

<style scoped>

.report {
    padding: 40px;
}

.report h1 {
    color: #003c71;
    font-size: 42px;
    margin-bottom: 10px;
}

.subtitle {
    color: #666;
    margin-bottom: 30px;
}

.report-card {
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow:
        0 2px 10px rgba(0,0,0,0.1);
}

.report-card h2 {
    color: #003c71;
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background: #003c71;
    color: white;
    padding: 12px;
    text-align: left;
}

td {
    padding: 12px;
    border-bottom:
        1px solid #e5e5e5;
}

.empty-state {
    background: white;
    padding: 25px;
    border-radius: 10px;
}

</style>