<template>

  <div class="compare">

    <h1>Compare Runs</h1>

    <p class="subtitle">
      Compare the latest two benchmark executions.
    </p>

    <div
      v-if="!compareData.latest"
      class="empty-state"
    >
      Not enough data available for comparison.
    </div>

    <div
      v-else
      class="compare-card"
    >

      <table>

        <thead>

          <tr>
            <th>Metric</th>
            <th>Previous</th>
            <th>Latest</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="(value, key) in compareData.latest"
            :key="key"
          >

            <td>{{ key }}</td>

            <td>
              {{
                compareData.previous
                  ? compareData.previous[key]
                  : "-"
              }}
            </td>

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

const compareData = ref({});

onMounted(async () => {

    try {

        const workload =
            route.params.workload;

        const response =
            await api.get(
                `/compare/${workload}`
            );

        compareData.value =
            response.data;

    } catch (error) {

        console.error(
            "Failed to load comparison",
            error
        );

    }

});

</script>

<style scoped>

.compare {
    padding: 40px;
}

.compare h1 {
    color: #003c71;
    font-size: 42px;
    margin-bottom: 10px;
}

.subtitle {
    color: #666;
    margin-bottom: 30px;
}

.compare-card {
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow:
        0 2px 10px rgba(0,0,0,0.1);
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
    color: #666;
}

</style>