<template>

  <div class="workloads">

    <h1>Registered Workloads</h1>

    <p class="subtitle">
      Available benchmark workloads configured in the platform.
    </p>

    <div class="workload-grid">

      <div
        v-for="workload in workloads"
        :key="workload.name"
        class="workload-card"
      >

        <h3>{{ workload.name }}</h3>

        <p>
          <strong>Stack:</strong>
          {{ workload.stack }}
        </p>

        <p>
          {{ workload.description }}
        </p>

        <p>
          <strong>Targets:</strong>
          {{ workload.supported_targets.join(", ") }}
        </p>

        <div class="actions">

          <button>
            History
          </button>

          <button>
            Compare
          </button>

          <button>
            Report
          </button>

        </div>

      </div>

    </div>

  </div>

</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const workloads = ref([]);

onMounted(async () => {

    try {

        const response = await api.get(
            "/workloads"
        );

        workloads.value =
            response.data.workloads;

    } catch (error) {

        console.error(
            "Failed to load workloads:",
            error
        );

    }

});
</script>

<style scoped>

.workloads {
    padding: 40px;
}

.workloads h1 {
    color: #003c71;
    margin-bottom: 10px;
    font-size: 48px;
}

.subtitle {
    color: #666;
    margin-bottom: 30px;
    font-size: 18px;
}

.workload-grid {
    display: grid;
    grid-template-columns:
        repeat(auto-fit, minmax(350px, 1fr));
    gap: 25px;
}

.workload-card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    border-left: 6px solid #003c71;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    transition: 0.2s;
}

.workload-card:hover {
    transform: translateY(-3px);
}

.workload-card h3 {
    color: #003c71;
    margin-bottom: 20px;
    font-size: 20px;
}

.workload-card p {
    margin-bottom: 12px;
    line-height: 1.5;
}

.actions {
    margin-top: 20px;
    display: flex;
    gap: 10px;
}

.actions button {
    background: #003c71;
    color: white;
    border: none;
    padding: 10px 16px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
    transition: 0.2s;
}

.actions button:hover {
    background: #0055a5;
}

</style>