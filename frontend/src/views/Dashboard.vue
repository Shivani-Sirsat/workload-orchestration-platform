<template>

  <div class="dashboard">

    <section class="hero">

      <h1>Workload Orchestration Platform</h1>

      <p>
        Execute, monitor and analyze benchmark workloads
        across Docker and Kubernetes environments.
      </p>

    </section>

    <section class="summary">

      <div class="summary-card">

        <h3>Total Workloads</h3>

        <p>
          {{ totalWorkloads }}
        </p>

      </div>

      <div class="summary-card">

        <h3>API Status</h3>

        <p>
          {{ apiStatus }}
        </p>

      </div>

      <div class="summary-card">

        <h3>Database</h3>

        <p>
          {{ dbStatus }}
        </p>

      </div>

    </section>

    <section class="capabilities">

      <h2>Key Capabilities</h2>

      <div class="capability-grid">

        <div class="capability-card">
          <h3>Execute Workloads</h3>
          <p>
            Run benchmark workloads using Docker
            and Kubernetes execution engines.
          </p>
        </div>

        <div class="capability-card">
          <h3>Historical Analysis</h3>
          <p>
            Review workload execution history
            stored in PostgreSQL.
          </p>
        </div>

        <div class="capability-card">
          <h3>KPI Reporting</h3>
          <p>
            Generate benchmark KPI reports
            from collected metrics.
          </p>
        </div>

        <div class="capability-card">
          <h3>Compare Benchmark Runs</h3>
          <p>
            Compare latest and previous workload
            executions side by side.
          </p>
        </div>

        <div class="capability-card">
          <h3>PostgreSQL Storage</h3>
          <p>
            Persist execution results
            in PostgreSQL.
          </p>
        </div>

        <div class="capability-card">
          <h3>REST APIs</h3>
          <p>
            Access workload data through
            FastAPI endpoints.
          </p>
        </div>

      </div>

    </section>

    <section class="stack">

      <h2>Technology Stack</h2>

      <div class="stack-grid">

        <div class="stack-card">Docker</div>
        <div class="stack-card">Kubernetes</div>
        <div class="stack-card">FastAPI</div>
        <div class="stack-card">PostgreSQL</div>
        <div class="stack-card">Vue.js</div>

      </div>

    </section>

  </div>

</template>

<script setup>

import { ref, onMounted } from "vue";
import api from "../services/api";

const totalWorkloads = ref(0);
const apiStatus = ref("Unknown");
const dbStatus = ref("Connected");

onMounted(async () => {

    try {

        const response =
            await api.get("/workloads");

        totalWorkloads.value =
            response.data.workloads.length;

        apiStatus.value =
            "Healthy";

    } catch (error) {

        console.error(error);

        apiStatus.value =
            "Unavailable";

        dbStatus.value =
            "Unknown";

    }

});

</script>

<style scoped>

.dashboard {
    padding: 40px;
    background: #f5f7fa;
    min-height: 100vh;
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
    color: #555;
    font-size: 18px;
}

.summary {
    display: flex;
    gap: 20px;
    margin-bottom: 40px;
}

.summary-card {
    flex: 1;
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.summary-card h3 {
    color: #003c71;
    margin-bottom: 10px;
}

.summary-card p {
    font-size: 32px;
    font-weight: bold;
    color: #003c71;
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
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.capability-card {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.capability-card h3 {
    color: #003c71;
    margin-bottom: 10px;
}

.capability-card p {
    color: #555;
    line-height: 1.6;
}

.stack h2 {
    color: #003c71;
    margin-bottom: 20px;
}

.stack-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
}

.stack-card {
    background: white;
    padding: 15px 25px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    font-weight: 600;
    color: #003c71;
}

@media (max-width: 900px) {

    .summary {
        flex-direction: column;
    }

    .capability-grid {
        grid-template-columns: 1fr;
    }

}

</style>