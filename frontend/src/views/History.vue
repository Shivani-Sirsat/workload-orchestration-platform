<template>

  <div class="history">

    <h1>History</h1>

    <p class="subtitle">
      Historical benchmark executions.
    </p>

    <div
      v-if="history.length === 0"
      class="empty-state"
    >
      No execution history found.
    </div>

    <div
      v-for="run in history"
      :key="run.run"
      class="history-card"
    >

      <h3>
        Run: {{ run.run }}
      </h3>

      <table>

        <thead>
          <tr>
            <th>KPI</th>
            <th>Value</th>
          </tr>
        </thead>

        <tbody>

          <tr
            v-for="(value, key) in run.kpis"
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

const history = ref([]);

onMounted(async () => {

    try {

        const workload =
            route.params.workload;

        const response =
            await api.get(
                `/history/${workload}`
            );

        history.value =
            response.data;

    } catch (error) {

        console.error(
            "Failed to load history",
            error
        );

    }

});

</script>

<style scoped>

.history {
    padding: 40px;
}

.history h1 {
    color: #003c71;
    font-size: 42px;
    margin-bottom: 10px;
}

.subtitle {
    color: #666;
    margin-bottom: 30px;
}

.history-card {
    background: white;
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow:
        0 2px 10px rgba(0,0,0,0.1);
}

.history-card h3 {
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
    text-align: left;
    padding: 12px;
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
    color: #666;
}

</style>