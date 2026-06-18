<template>

  <div class="dashboard">

    <section class="hero">

      <h1>Workload Orchestration Platform</h1>

      <p>
        Execute, monitor and analyze benchmark workloads
        across multiple execution environments.
      </p>

    </section>

    <section class="summary">

      <div class="summary-card">
        <h3>Registered Workloads</h3>
        <p>{{ workloads.length }}</p>
      </div>

      <div class="summary-card">
        <h3>API Status</h3>
        <p>Healthy</p>
      </div>

      <div class="summary-card">
        <h3>Database</h3>
        <p>Connected</p>
      </div>

    </section>

    <section class="capabilities">

      <h2>Key Capabilities</h2>

      <div class="capability-grid">

        <div class="capability-card">
          <h3>Workload Execution</h3>
          <p>
            Execute benchmark workloads on
            Docker and Kubernetes platforms.
          </p>
        </div>

        <div class="capability-card">
          <h3>Benchmark Reporting</h3>
          <p>
            Generate KPI reports for completed
            workload executions.
          </p>
        </div>

        <div class="capability-card">
          <h3>Historical Analysis</h3>
          <p>
            View workload execution history
            stored in PostgreSQL.
          </p>
        </div>

        <div class="capability-card">
          <h3>KPI Comparison</h3>
          <p>
            Compare recent workload runs
            and benchmark performance.
          </p>
        </div>

        <div class="capability-card">
          <h3>REST APIs</h3>
          <p>
            Access workloads, history,
            reports and comparison data.
          </p>
        </div>

        <div class="capability-card">
          <h3>PostgreSQL Storage</h3>
          <p>
            Persist benchmark executions
            and KPI results in database.
          </p>
        </div>

      </div>

    </section>

    <section class="platform">

      <h2>Supported Components</h2>

      <ul>
        <li>Docker Execution Engine</li>
        <li>Kubernetes Execution Engine</li>
        <li>PostgreSQL Result Storage</li>
        <li>FastAPI Backend Services</li>
        <li>Vue.js Frontend Dashboard</li>
      </ul>

    </section>

  </div>

</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const workloads = ref([]);

onMounted(async () => {

    const response = await api.get(
        "/workloads"
    );

    workloads.value = response.data;

});
</script>

<style scoped>

.dashboard {
    padding: 40px;
}

.hero {
    margin-bottom: 40px;
}

.hero h1 {
    color: #003c71;
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #555;
}

.summary {
    display: flex;
    gap: 20px;
    margin-bottom: 50px;
}

.summary-card {
    flex: 1;
    background: white;
    border-radius: 10px;
    padding: 25px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.summary-card h3 {
    color: #003c71;
}

.summary-card p {
    font-size: 32px;
    font-weight: bold;
    margin-top: 15px;
}

.capabilities {
    margin-bottom: 50px;
}

.capabilities h2 {
    color: #003c71;
    margin-bottom: 20px;
}

.capability-grid {
    display: grid;
    grid-template-columns:
        repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

.capability-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.capability-card h3 {
    color: #003c71;
    margin-bottom: 10px;
}

.platform h2 {
    color: #003c71;
    margin-bottom: 15px;
}

.platform ul {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.platform li {
    margin-bottom: 10px;
}

</style>