# Workload Orchestration Platform

A full-stack benchmark automation platform built using Python, FastAPI, PostgreSQL, Docker, Kubernetes, and Vue.js.

The platform enables workload discovery, benchmark execution, KPI collection, result persistence, historical analysis, benchmark comparison, and reporting through a modern web dashboard.

---

## Features

### Workload Management

* Dynamic workload discovery using metadata
* Centralized workload registry
* Support for multiple benchmark workloads

### Execution Engine

* Docker-based workload execution
* Kubernetes-based workload execution
* Unified execution framework

### Result Collection

* Automated KPI extraction
* Benchmark log collection
* JSON result storage

### PostgreSQL Integration

* Benchmark run persistence
* KPI metric storage
* Historical benchmark tracking

### Analytics APIs

* Workload APIs
* History APIs
* Comparison APIs
* Reporting APIs
* Health monitoring APIs

### Web Dashboard

* Workload Management
* Historical Analysis
* KPI Comparison
* Benchmark Reporting
* Platform Monitoring

---

## Supported Workloads

| Workload               | Target     |
| ---------------------- | ---------- |
| redis-benchmark        | Docker     |
| tpcc-postgresql        | Kubernetes |
| kafka-stream-benchmark | Planned    |
| spark-terasort         | Planned    |
| ycsb-mongodb           | Planned    |

---

## Architecture

```text
Vue.js Dashboard
        │
        ▼
FastAPI REST APIs
        │
        ▼
Execution Engine
   ┌─────────────┐
   │             │
   ▼             ▼
Docker      Kubernetes
   │             │
   └──────┬──────┘
          ▼
Result Collection
          ▼
PostgreSQL Storage
          ▼
Analytics APIs
```

---

## Technology Stack

### Backend

* Python
* FastAPI

### Database

* PostgreSQL

### Container Platforms

* Docker
* Kubernetes

### Frontend

* Vue.js
* Axios
* Vue Router

### Infrastructure

* Kubernetes Services
* Docker Containers

---

## REST APIs

### Health

```http
GET /api/v1/health
```

### Workloads

```http
GET /api/v1/workloads
```

### History

```http
GET /api/v1/history/{workload}
```

### Compare

```http
GET /api/v1/compare/{workload}
```

### Report

```http
GET /api/v1/report/{workload}
```

---

## Project Structure

```text
workload-orchestration-platform/

├── api/
├── cli/
├── database/
├── execution/
├── frontend/
├── workloads/
├── stacks/
├── results/
└── logs/
```

---

## Dashboard Capabilities

### Dashboard

* Platform overview
* Technology stack visibility
* Platform capabilities

### Workloads

* Registered workload discovery
* Workload metadata display

### History

* Historical benchmark executions
* KPI visualization

### Compare

* Previous vs latest benchmark comparison

### Report

* Benchmark KPI reporting

---

## Example Workflow

```text
1. Execute Benchmark
       ↓
2. Collect KPIs
       ↓
3. Store Results
       ↓
4. Persist to PostgreSQL
       ↓
5. Generate Analytics
       ↓
6. Visualize in Dashboard
```

---

## Key Achievements

* Built a full-stack benchmark orchestration platform
* Integrated Docker and Kubernetes execution environments
* Implemented PostgreSQL-backed KPI persistence
* Developed FastAPI analytics services
* Built Vue.js analytics dashboard
* Enabled benchmark history, comparison, and reporting workflows

---

## Future Enhancements

* UI-based workload execution
* KPI trend visualizations
* Authentication and authorization
* Asynchronous workload scheduling
* Multi-cluster execution support
* Real-time benchmark monitoring
