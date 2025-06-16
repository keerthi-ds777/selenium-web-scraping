# Redbus Data Scraping & Dynamic Filtering System

## 📌 Overview
This project automates extraction of bus transportation data from Redbus using Selenium, stores it in a SQL database, and provides an interactive Streamlit interface for dynamic filtering. Designed for transportation industry analytics, it enables real-time analysis of routes, pricing, and availability across government and private bus services.

## 🛠 Skills Utilized
- **Web Scraping** with Selenium
- **Python** Data Processing
- **SQL** Database Management
- **Streamlit** Dashboard Development
- **Data Analysis** & Visualization

## 🚀 Key Features
- **10+ Data Points** per bus route including pricing, ratings, and seat availability
- **Real-time Filters** for bustype, price range (₹500-₹2000), star ratings (1-5), and seat availability
- **Comparative Analysis** of government vs private transport services
- **Dynamic SQL Queries** for instant data retrieval

## 🗄 Database Schema
| Column          | Type    | Description                          |
|-----------------|---------|--------------------------------------|
| id              | INT     | Auto-incrementing primary key        |
| route_name      | TEXT    | Mumbai-Pune, Delhi-Jaipur etc.       |
| bustype         | TEXT    | Sleeper/Seater/AC/Non-AC             |
| departing_time  | TIME    | Departure timestamp (24h format)     |
| price           | DECIMAL | Ticket price (₹)                     |
| seats_available | INT     | Real-time seat inventory             |

## 🖥 Streamlit Interface

