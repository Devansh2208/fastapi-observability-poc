# EKS Observability Platform

## Overview

The EKS Observability Platform provides a centralized monitoring and logging solution for FastAPI-based applications deployed on Amazon EKS.

The platform enables product teams to onboard services with minimal effort while automatically receiving:

* Application Monitoring
* Infrastructure Monitoring
* Grafana Dashboards
* Prometheus Metrics Collection
* CloudWatch Logs
* CloudWatch Container Insights
* Kubernetes Health Monitoring

---

# Architecture

```text
                           Internet
                               │
                               ▼

                    AWS Load Balancer
                               │

       ┌──────────────────────────────────────┐
       │              Amazon EKS              │
       │                                      │
       │   FastAPI Application Pods           │
       │                                      │
       │   Prometheus                         │
       │   Grafana                            │
       │                                      │
       └──────────────────────────────────────┘
                 │                     │

                 ▼                     ▼

         CloudWatch Logs      Container Insights

                 │

          CloudWatch Agent
              Fluent Bit
```

---

# Platform Components

## Amazon EKS

Container orchestration platform responsible for:

* Pod Scheduling
* High Availability
* Self Healing
* Horizontal Scaling

---

## Prometheus

Collects:

* Application Metrics
* Pod Metrics
* Namespace Metrics
* Cluster Metrics

---

## Grafana

Visualizes:

* Application Dashboards
* Infrastructure Dashboards
* Cluster Dashboards

---

## CloudWatch Logs

Stores:

* Application Logs
* Container Logs
* Node Logs

---

## CloudWatch Container Insights

Provides:

* Node Metrics
* Pod Metrics
* Deployment Metrics
* Namespace Metrics

---

# Repository Structure

```text
observability-platform/

├── eks/
│   ├── cluster.yaml
│   └── nodegroup.yaml
│
├── monitoring/
│   ├── prometheus-values.yaml
│   ├── grafana-values.yaml
│   └── alertmanager-values.yaml
│
├── cloudwatch/
│   ├── cloudwatch-setup.md
│   ├── pod-identity.md
│   └── iam-policies.md
│
├── onboarding/
│   └── templates/
│       ├── Dockerfile
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── servicemonitor.yaml
│       └── namespace.yaml
│
├── docs/
│   ├── architecture.md
│   ├── deployment-guide.md
│   ├── onboarding-guide.md
│   ├── demo-runbook.md
│   └── cost-estimation.md
│
└── README.md
```

---

# Product Onboarding

To onboard a FastAPI application, the product team must provide:

* Source Code Repository
* Docker Build Instructions
* Application Port
* Environment Variables
* Health Endpoint
* Metrics Endpoint
* CPU/Memory Requirements
* Replica Requirements

After onboarding, the platform automatically provides:

✓ Prometheus Monitoring

✓ Grafana Dashboards

✓ CloudWatch Logs

✓ Container Insights

✓ Kubernetes Monitoring

---

# Current Access Model

Development

Grafana:

```bash
kubectl port-forward -n monitoring svc/kube-prometheus-stack-grafana 3000:80
```

Prometheus:

```bash
kubectl port-forward -n monitoring svc/kube-prometheus-stack-prometheus 9090:9090
```

Application:

```bash
kubectl port-forward -n observability-poc svc/fastapi-service 8000:80
```

---

# Production Access Model

Grafana:

```text
http://grafana.company.com
```

FastAPI Services:

```text
http://service.company.com
```

Prometheus:

Internal Only

CloudWatch:

AWS Console

---

# Success Criteria

Platform is considered healthy when:

* EKS Nodes Ready
* Prometheus Targets UP
* Grafana Accessible
* CloudWatch Logs Available
* Container Insights Available
* Application Metrics Visible

