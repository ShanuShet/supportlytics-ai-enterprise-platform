/********************************************************************
    Supportlytics AI Enterprise
    app.js
    Part 1
********************************************************************/

const API_BASE = "http://127.0.0.1:8000";

let dashboardData = {};

let tickets = [];

let selectedTicket = null;

let priorityChart = null;

let currentTab = "dashboard";

let statusChart;

let categoryChart;

let trendChart;

let activityCounter = 0;

// =======================================================
// APPLICATION START
// =======================================================

document.addEventListener(

    "DOMContentLoaded",

    () => {

        initializeApplication();

    }

);


// =======================================================
// INITIALIZE
// =======================================================

async function initializeApplication(){

    showLoadingScreen();

    initializeNavigation();

    initializeButtons();

    initializeSearch();

    initializeFilters();

    await heartbeat();

    await loadDashboard();

    await loadTickets();

    await loadAnalytics();

    connectWebSocket();

    startLiveClock();

    animateWorkflow();

    addActivity("Supportlytics AI Started");

}

// =======================================================
// NAVIGATION
// =======================================================

function initializeNavigation() {

    const links = document.querySelectorAll(".nav-link");
    const pages = document.querySelectorAll(".tab-page");

    links.forEach(link => {

        link.addEventListener("click", function (e) {

            // Prevent <a> from navigating
            e.preventDefault();

            console.log("Clicked:", this.dataset.tab);

            links.forEach(item => item.classList.remove("active"));

            pages.forEach(page => page.classList.remove("active"));

            this.classList.add("active");

            const page = document.getElementById("tab-" + this.dataset.tab);

            console.log(page);

            if (page) {
                page.classList.add("active");
            } else {
                console.error("Tab not found:", "tab-" + this.dataset.tab);
            }

            currentTab = this.dataset.tab;

            switch (currentTab) {

                case "dashboard":
                    loadDashboard();
                    break;

                case "tickets":
                    loadTickets();
                    break;

                case "analytics":
                    loadAnalytics();
                    break;
            }

        });

    });

}
// =======================================================
// BUTTONS
// =======================================================

function initializeButtons(){

    document.getElementById(

        "btn-refresh"

    )?.addEventListener(

        "click",

        refreshDashboard

    );

    document.getElementById(

        "btn-refresh-tickets"

    )?.addEventListener(

        "click",

        loadTickets

    );

}

// =======================================================
// HEARTBEAT
// =======================================================

async function heartbeat(){

    try{

        const response=

            await fetch(

                API_BASE+"/"

            );

        if(response.ok){

            document.getElementById(

                "server-status"

            ).innerHTML="ONLINE";

        }

        else{

            document.getElementById(

                "server-status"

            ).innerHTML="OFFLINE";

        }

    }

    catch(error){

        document.getElementById(

            "server-status"

        ).innerHTML="OFFLINE";

    }

}

// =======================================================
// DASHBOARD API
// =======================================================

async function loadDashboard(){

    try{

        const response=

            await fetch(

                API_BASE+"/dashboard/"

            );

        dashboardData=

            await response.json();
            addActivity("Dashboard manually refreshed.");

        renderMetrics();

        renderCategories();

        renderPriorityChart();

        updateAIHealth();

    }

    catch(error){

        console.error(error);

    }

}

// =======================================================
// METRICS
// =======================================================

function renderMetrics(){

    if(!dashboardData.overview){
        return;
    }

    const o = dashboardData.overview;

    animateMetric(
        "metric-total-tickets",
        o.totalTicketsProcessed
    );

    animateMetric(
        "metric-resolved",
        o.autoResolved
    );

    animateMetric(
        "metric-hitl-count",
        o.hitlHolds
    );

    animateMetric(
        "metric-security-blocks",
        o.blockedThreats
    );

    animateMetric(
        "metric-resolution-rate",
        o.resolutionRate + "% Resolved"
    );

    animateMetric(
        "metric-live-status",
        "Updated Live"
    );

}

// =======================================================
// CATEGORY LIST
// =======================================================

function renderCategories(){

    const list=

        document.getElementById(

            "category-distribution-list"

        );

    if(!list){

        return;

    }

    list.innerHTML="";

    if(!dashboardData.categories){

        return;

    }

    dashboardData.categories.forEach(

        category=>{

            list.innerHTML+=`

            <div class="cat-item">

                <span class="cat-name">

                    ${category.category}

                </span>

                <span class="cat-count">

                    ${category.count}

                </span>

            </div>

            `;

        }

    );

}

// =======================================================
// PRIORITY CHART
// =======================================================

function renderPriorityChart(){

    if(!dashboardData.priorities){

        return;

    }

    const canvas = document.getElementById(

        "priorityChart"

    );

    if(!canvas){

        return;

    }

    const labels = [];

    const values = [];

    dashboardData.priorities.forEach(item=>{

        labels.push(item.priority);

        values.push(item.count);

    });

    if(priorityChart){

        priorityChart.destroy();

    }

    priorityChart = new Chart(

        canvas,

        {

            type:"bar",

            data:{

                labels:labels,

                datasets:[{

                    label:"Tickets",

                    data:values,

                    borderWidth:1,

                    borderRadius:8

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{

                        display:false

                    }

                },

                scales:{

                    y:{

                        beginAtZero:true

                    }

                }

            }

        }

    );

}

function updateAIHealth(){

    const health =
        document.getElementById("ai-health");

    if(!health){
        return;
    }

    const total =
        dashboardData.overview.totalTicketsProcessed;

    const blocked =
        dashboardData.overview.blockedThreats;

    if(blocked>0){

        health.innerHTML="⚠ Warning";

        health.style.color="#F59E0B";

    }

    else if(total>0){

        health.innerHTML="🟢 Healthy";

        health.style.color="#22C55E";

    }

    else{

        health.innerHTML="🔴 Offline";

        health.style.color="#EF4444";

    }

}

// =======================================================
// LOAD TICKETS
// =======================================================

async function loadTickets(){

    try{

        const response = await fetch(

            API_BASE + "/tickets/"

        );

        tickets = await response.json();

        renderTicketCards();

        const filter = document.getElementById("priority-filter");

        if (filter) {
            filter.value = "ALL";
        }

        setText(

            "ticket-count",

            tickets.length

        );

    }

    catch(error){

        console.error(error);

    }

}

// =======================================================
// RENDER TICKET LIST
// =======================================================

function renderTicketCards(){

    const container = document.getElementById(

        "ticket-cards-list"

    );

    if(!container){

        return;

    }

    container.innerHTML="";

    if(tickets.length===0){

        container.innerHTML=`

        <div class="ticket-card-item">

            No Tickets Found

        </div>

        `;

        return;

    }

    tickets.forEach(ticket=>{

        container.innerHTML+=`

        <div

            class="ticket-card-item"

            onclick="showTicket('${ticket.ticket_id}')">

            <div class="ticket-card-header">

                <div class="ticket-id">

                    ${ticket.ticket_id}

                </div>

                <div class="badge-status ${ticket.status}">

                    ${ticket.status}

                </div>

            </div>

            <div class="ticket-card-title">

                ${ticket.title}

            </div>

            <div class="ticket-card-meta">

                <span>

                    ${ticket.category}

                </span>

                <span>

                    ${ticket.country}

                </span>

            </div>

        </div>

        `;

    });

}

// =======================================================
// SHOW TICKET
// =======================================================

function showTicket(ticketId){

    const ticket = tickets.find(
        t => t.ticket_id === ticketId
    );

    if(!ticket){
        return;
    }

    addActivity(
        "Viewing Ticket " + ticket.ticket_id
    );

    selectedTicket = ticket;

    const panel =
        document.getElementById(
            "ticket-detail-view"
        );

    panel.innerHTML = `
    <div class="detail-header">

        <div class="detail-title">
            ${ticket.title}
        </div>

        <div class="detail-tags">

            <div class="tag-badge">
                ${formatText(ticket.priority)}
            </div>

            <div class="tag-badge">
                ${formatText(ticket.status)}
            </div>

            <div class="tag-badge">
                ${ticket.country}
            </div>

        </div>

    </div>

    <p style="margin-bottom:20px;">
        ${ticket.description}
    </p>

    <div class="detail-section-title">
        Ticket Information
    </div>

    <table style="width:100%;border-spacing:10px;">

        <tr>
            <td><strong>Ticket ID</strong></td>
            <td>${ticket.ticket_id}</td>
        </tr>

        <tr>
            <td><strong>Category</strong></td>
            <td>${formatText(ticket.category)}</td>
        </tr>

        <tr>
            <td><strong>Department</strong></td>
            <td>${formatText(ticket.department)}
        </tr>

        <tr>
            <td><strong>Assigned Team</strong></td>
            <td>${ticket.assigned_team}</td>
        </tr>

        <tr>
            <td><strong>User</strong></td>
            <td>${ticket.user_name}</td>
        </tr>

        <tr>
            <td><strong>Risk Score</strong></td>
            <td>${(ticket.risk_score ?? 0).toFixed(2)}</td>
        </tr>

    </table>

    <div class="detail-section-title">
        AI Agent Decision Trace
    </div>

    <div class="trace-timeline">

        <div class="trace-step-card agent-trace">

            <div class="step-agent-name">
                Ticket Ingestion Agent
            </div>

            <div class="step-details">
                Ticket received successfully.
            </div>

        </div>

        <div class="trace-step-card agent-trace">

            <div class="step-agent-name">
                Classification Agent
            </div>

            <div class="step-details">
                Classified as
                <strong>${formatText(ticket.category)}</strong>
            </div>

        </div>

        <div class="trace-step-card agent-trace">

            <div class="step-agent-name">
                Priority Prediction Agent
            </div>

            <div class="step-details">
                Predicted priority:
                <strong>${formatText(ticket.priority)}</strong>
            </div>

        </div>

        <div class="trace-step-card agent-trace">

            <div class="step-agent-name">
                Human Approval Agent
            </div>

            <div class="step-details">
                Current Status:
                <strong>${formatText(ticket.status)}</strong>
            </div>

        </div>

    </div>
    `;

    animateTraceTimeline();
}

// =======================================================
// SEARCH TICKETS
// =======================================================

function initializeSearch(){

    const searchBox=document.getElementById("ticket-search");

    if(searchBox){

        searchBox.addEventListener("keyup",(e)=>{

            searchTickets(e.target.value);

        });

    }

}

function searchTickets(keyword){

    keyword = keyword.toLowerCase();

    const filtered = tickets.filter(ticket=>{

        return(

            ticket.title.toLowerCase().includes(keyword)

            ||

            ticket.ticket_id.toLowerCase().includes(keyword)

            ||

            ticket.category.toLowerCase().includes(keyword)

            ||

            ticket.country.toLowerCase().includes(keyword)

        );

    });

    renderFilteredTickets(filtered);

}

// =======================================================
// FILTERED LIST
// =======================================================

function renderFilteredTickets(list){

    const container = document.getElementById(

        "ticket-cards-list"

    );

    if(!container){

        return;

    }

    container.innerHTML="";

    if(list.length===0){

        container.innerHTML=`

        <div class="ticket-card-item">

            No Matching Ticket

        </div>

        `;

        return;

    }

    list.forEach(ticket=>{

        container.innerHTML+=`

        <div

        class="ticket-card-item"

        onclick="showTicket('${ticket.ticket_id}')">

            <div class="ticket-card-header">

                <div class="ticket-id">

                    ${ticket.ticket_id}

                </div>

                <div class="badge-status ${ticket.status}">

                    ${ticket.status}

                </div>

            </div>

            <div class="ticket-card-title">

                ${ticket.title}

            </div>

            <div class="ticket-card-meta">

                <span>

                    ${ticket.category}

                </span>

                <span>

                    ${ticket.country}

                </span>

            </div>

        </div>

        `;

    });

}

// =======================================================
// PRIORITY FILTER
// =======================================================

function initializeFilters(){

    showLoadingScreen();

    const priorityFilter=document.getElementById("priority-filter");

    if(priorityFilter){

        priorityFilter.addEventListener("change",(e)=>{

            filterPriority(e.target.value);

        });

    }

}

function filterPriority(priority){

    if(priority.toUpperCase() === "ALL"){

        renderTicketCards();

        return;

    }

    const filtered = tickets.filter(ticket =>

        ticket.priority &&
        ticket.priority.toUpperCase() === priority.toUpperCase()

    );

    renderFilteredTickets(filtered);

}

// =======================================================
// LOAD ANALYTICS
// =======================================================

async function loadAnalytics(){

    try{

        const dashboardResponse =
            await fetch(API_BASE + "/dashboard/");

        const dashboardData =
            await dashboardResponse.json();

        document.getElementById("analytics-total").innerHTML =
            dashboardData.overview.totalTicketsProcessed;

        document.getElementById("analytics-open").innerHTML =
            dashboardData.overview.totalTicketsProcessed -
            dashboardData.overview.autoResolved;

        document.getElementById("analytics-closed").innerHTML =
            dashboardData.overview.autoResolved;

        const rate =
            (
                dashboardData.overview.autoResolved /
                dashboardData.overview.totalTicketsProcessed
            ) * 100;

        document.getElementById("analytics-rate").innerHTML =
            rate.toFixed(1) + "%";

        drawStatusChart(dashboardData.overview);
        drawPriorityChart(dashboardData.priorities);
        drawCategoryChart(dashboardData.categories);
        drawTrendChart();
        renderAIInsights();

    }

    catch(error){

        console.error(error);

    }

}


function drawStatusChart(data){

    const ctx =
        document.getElementById("statusChart");

    if(statusChart){

        statusChart.destroy();

    }

    statusChart =
        new Chart(ctx,{

            type:"doughnut",

            data:{

                labels:[
                    "Open",
                    "In Progress",
                    "Pending",
                    "Resolved"
                ],

                datasets:[{

                    data:[
                        data.openTickets,
                        data.inProgress,
                        data.pendingTickets,
                        data.autoResolved
                    ],

                    backgroundColor:[
                        "#3B82F6",
                        "#F59E0B",
                        "#A855F7",
                        "#22C55E"
                    ]

                }]

            },

            options:{

                animation:{

                    duration:1200,

                    easing:"easeOutQuart"

                },

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{
                        labels:{
                            color:"#ffffff"
                        }
                    }

                }

            }

        });

}
function drawPriorityChart(data){

    const order = [

        "critical",
        "high",
        "medium",
        "low"

    ];

    data.sort(

        (a,b)=>

        order.indexOf(a.priority.toLowerCase())-

        order.indexOf(b.priority.toLowerCase())

    );

    const ctx =
        document.getElementById("analyticsPriorityChart");

    if(priorityChart){

        priorityChart.destroy();

    }

    priorityChart =
        new Chart(ctx,{

            type:"bar",

            data:{

                labels:data.map(

                    p=>p.priority

                ),

                datasets:[{

                    label:"Tickets",

                    data:data.map(

                        p=>p.count

                    ),

                    backgroundColor:"#6C63FF",

                    borderRadius:8

                }]

            },

            options:{

                animation:{

                    duration:1200,

                    easing:"easeOutQuart"

                },

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{
                        display:false
                    }

                },

                scales:{

                    y:{
                        beginAtZero:true,
                        ticks:{
                            color:"#ffffff"
                        }
                    },

                    x:{
                        ticks:{
                            color:"#ffffff"
                        }
                    }

                }

            }

        });

}
function drawCategoryChart(data){

    data.sort(

        (a,b)=>b.count-a.count

    );

    const ctx =
        document.getElementById("categoryChart");

    if(categoryChart){

        categoryChart.destroy();

    }

    categoryChart =
        new Chart(ctx,{

            type:"bar",

            data:{

                labels:data.map(

                    c=>c.category

                ),

                datasets:[{

                    label:"Tickets",

                    data:data.map(

                        c=>c.count

                    ),

                    backgroundColor:"#38BDF8",

                    borderRadius:8

                }]

            },

            options:{

                animation:{

                    duration:1200,

                    easing:"easeOutQuart"

                },

                indexAxis:"y",

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{
                        display:false
                    }

                },

                scales:{

                    x:{
                        beginAtZero:true,
                        ticks:{
                            color:"#ffffff"
                        }
                    },

                    y:{
                        ticks:{
                            color:"#ffffff"
                        }
                    }

                }

            }

        });

}

function drawTrendChart(){

    const ctx =
        document.getElementById("trendChart");

    if(trendChart){

        trendChart.destroy();

    }

    trendChart =
        new Chart(ctx,{

            type:"line",

            data:{

                labels:[
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun"
                ],

                datasets:[{

                    label:"Tickets",

                    data:[
                        25,
                        42,
                        67,
                        91,
                        133,
                        201
                    ],

                    borderColor:"#38BDF8",

                    backgroundColor:"rgba(56,189,248,.25)",

                    fill:true,

                    tension:.35

                }]

            },

            options:{

                animation:{

                    duration:1200,

                    easing:"easeOutQuart"

                },

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{
                        labels:{
                            color:"#ffffff"
                        }
                    }

                },

                scales:{

                    x:{
                        ticks:{
                            color:"#ffffff"
                        }
                    },

                    y:{
                        beginAtZero:true,
                        ticks:{
                            color:"#ffffff"
                        }
                    }

                }

            }

        });

}

// =======================================================
// COUNTRY ANALYTICS
// =======================================================

async function loadCountries(){

    try{

        const response =
        await fetch(
        API_BASE+"/dashboard/"
        );

        const dashboardData =
        await response.json();

        const countries =
        dashboardData.countries;

        updateAIHealth();
        renderCountries(countries);

    }

    catch(error){

        console.error(error);

    }

}

function renderCountries(data){

    const container = document.getElementById(

        "country-list"

    );

    if(!container){

        return;

    }

    container.innerHTML="";

    data.forEach(country=>{

        container.innerHTML+=`

        <div class="cat-item">

            <span class="cat-name">

                ${country.country}

            </span>

            <span class="cat-count">

                ${country.count}

            </span>

        </div>

        `;

    });

}

// =======================================================
// AI PREDICTION
// =======================================================

async function prediction(endpoint){

    const ticketId = document
        .getElementById(
            "prediction-ticket-id"
        )
        .value
        .trim();

    if(ticketId===""){

        openModal(
            "Please enter Ticket ID."
        );

        return;

    }

    try{

        const panel = document.getElementById(
            "prediction-result"
        );

        panel.innerHTML = `

        <div class="prediction-loading">

        🤖 AI Agent is analyzing ticket...

        </div>

        `;

        const response =
            await fetch(

                API_BASE +

                "/prediction/" +

                endpoint +

                "/" +

                ticketId

            );

        if (!response.ok) {
            const error = await response.json();
            openModal(error.detail || "Prediction Failed.");
            return;
        }

const result = await response.json();

        renderPredictionResult(endpoint, result);

        addActivity(
            endpoint.toUpperCase() +
            " prediction completed for " +
            result.ticket_id
        );

        showNotification(endpoint.toUpperCase() +" Prediction Completed");

        animateWorkflow();

    }

    catch(error){

        console.error(error);

        openModal(
            "Prediction Failed."
        );

    }

}

function renderPredictionResult(endpoint, data){

    const panel = document.getElementById(
        "prediction-result"
    );

    if(!panel){
        return;
    }

    let html = "";

    let recommendation = "";

    switch(endpoint){

        case "priority":

            switch(data.predicted_priority){

                case "CRITICAL":
                    recommendation =
                    "🚨 Escalate immediately to the Security Team and notify management.";
                    break;

                case "HIGH":
                    recommendation =
                    "⚡ Assign immediately to the appropriate support team.";
                    break;

                case "MEDIUM":
                    recommendation =
                    "📋 Schedule resolution during the current working shift.";
                    break;

                default:
                    recommendation =
                    "✅ Queue for normal SLA processing.";
            }

            html = `

            <div class="prediction-card">

                <h3>🎯 Priority Prediction</h3>

                <p>
                    <strong>Ticket ID</strong><br>
                    ${data.ticket_id}
                </p>

                <p>
                    <strong>Predicted Priority</strong><br>
                    ${data.predicted_priority}
                </p>

                <p>
                    <strong>Confidence</strong><br>
                    ${(data.confidence*100).toFixed(0)}%
                </p>

                <div class="prediction-recommendation">

                    <strong>🤖 AI Recommendation</strong>

                    <br><br>

                    ${recommendation}

                </div>

            </div>

            `;

            break;

        case "risk":

            if(data.risk_score >= 0.90){

                recommendation =
                "🚨 High security risk. Escalate immediately.";

            }

            else if(data.risk_score >= 0.70){

                recommendation =
                "⚠ Monitor continuously until resolved.";

            }

            else if(data.risk_score >= 0.40){

                recommendation =
                "📋 Normal monitoring is sufficient.";

            }

            else{

                recommendation =
                "✅ Minimal operational risk.";

            }

            html = `

            <div class="prediction-card">

                <h3>🛡 Risk Prediction</h3>

                <p>
                    <strong>Ticket ID</strong><br>
                    ${data.ticket_id}
                </p>

                <p>
                    <strong>Risk Score</strong><br>
                    ${data.risk_score}
                </p>

                <p>
                    <strong>Risk Level</strong><br>
                    ${data.risk_level}
                </p>

                <div class="prediction-recommendation">

                    <strong>🤖 AI Recommendation</strong>

                    <br><br>

                    ${recommendation}

                </div>

            </div>

            `;

            break;

        case "sla":

            recommendation =
            "⏱ Ensure the ticket is resolved within the predicted SLA.";

            html = `

            <div class="prediction-card">

                <h3>⏰ SLA Prediction</h3>

                <p>
                    <strong>Ticket ID</strong><br>
                    ${data.ticket_id}
                </p>

                <p>
                    <strong>Predicted SLA</strong><br>
                    ${data.predicted_sla}
                </p>

                <div class="prediction-recommendation">

                    <strong>🤖 AI Recommendation</strong>

                    <br><br>

                    ${recommendation}

                </div>

            </div>

            `;

            break;

        case "resolution":

            recommendation =
            "🛠 Allocate resources to achieve the predicted resolution time.";

            html = `

            <div class="prediction-card">

                <h3>📈 Resolution Prediction</h3>

                <p>
                    <strong>Ticket ID</strong><br>
                    ${data.ticket_id}
                </p>

                <p>
                    <strong>Estimated Resolution Time</strong><br>
                    ${data.predicted_resolution_time}
                    ${data.unit}
                </p>

                <div class="prediction-recommendation">

                    <strong>🤖 AI Recommendation</strong>

                    <br><br>

                    ${recommendation}

                </div>

            </div>

            `;

            break;

    }

    panel.innerHTML = html;

    const recommendationBox =
        document.getElementById(
            "recommendation-box"
        );

    if(recommendationBox){

        recommendationBox.innerHTML = `
            <h4>🤖 AI Recommendation</h4>

            <br>

            Ticket
            <b>${data.ticket_id}</b>

            <br><br>

            Recommended Action

            <br>

            ⚡ Assign immediately to the corresponding support team.

            <br><br>

            Confidence

            <b>
            ${
                data.confidence
                    ? (data.confidence * 100).toFixed(0)
                    : "95"
            }%
            </b>
        `;

    }

}

// =======================================================
// PREDICTION BUTTONS
// =======================================================

document.getElementById(

    "btn-predict-priority"

)?.addEventListener(

    "click",

    ()=>prediction("priority")

);

document.getElementById(

    "btn-predict-risk"

)?.addEventListener(

    "click",

    ()=>prediction("risk")

);

document.getElementById(

    "btn-predict-sla"

)?.addEventListener(

    "click",

    ()=>prediction("sla")

);

document.getElementById(

    "btn-predict-resolution"

)?.addEventListener(

    "click",

    ()=>prediction(

        "resolution"

    )

);

document.getElementById(

    "btn-export-report"

)?.addEventListener(

    "click",

    exportReport

);

// =======================================================
// SIMULATOR
// =======================================================

async function simulator(action){

    try{

        const response = await fetch(

            API_BASE +

            "/simulator/" +

            action,

            {

                method:"POST"

            }

        );

        const result = await response.json();

        addActivity("Traffic Simulator generated 10 synthetic tickets.");

        const panel = document.getElementById("simulator-status");

        if(result.generated){

            panel.innerHTML = `

                <div class="sim-success">

                    <h3>✅ AI Traffic Simulator Started</h3>

                    <p>
                        Successfully generated
                        <strong>${result.generated}</strong>
                        synthetic IT tickets.
                    </p>

                    <br>

                    <strong>Generated Ticket IDs</strong>

                    <ul>

                        ${result.tickets
                            .map(id => `<li>${id}</li>`)
                            .join("")}

                    </ul>

                </div>

            `;

        }
        else{

            panel.innerHTML = `

                <div class="sim-success">

                    <h3>✅ ${result.status || "Completed"}</h3>

                </div>

            `;

        }

        addActivity(
            "Simulator " + action
        );

        if(action === "start"){

            showNotification(
                `${result.generated} tickets generated successfully.`
            );

        }
        else{

            showNotification(
                "Simulator stopped successfully."
            );

        }

        animateWorkflow();

        await loadDashboard();

        await loadTickets();

        await loadAnalytics();

    }

    catch(error){

        console.error(error);

    }

}

document.getElementById(

    "btn-start-simulator"

)?.addEventListener(

    "click",

    ()=>simulator("start")

);

document.getElementById(

    "btn-stop-simulator"

)?.addEventListener(

    "click",

    ()=>simulator("stop")

);

// =======================================================
// DATASET UPLOAD
// =======================================================

document.getElementById(

    "btn-upload"

)?.addEventListener(

    "click",

    uploadDataset

);

async function uploadDataset(){

    const file = document.getElementById(

        "dataset-file"

    ).files[0];

    if(!file){

        openModal(

            "Please select a dataset."

        );

        return;

    }

    const form = new FormData();

    form.append(

        "file",

        file

    );

    try{

        const response = await fetch(

            API_BASE +

            "/ingestion/upload",

            {

                method:"POST",

                body:form

            }

        );

        const result = await response.json();

        addActivity("Dataset uploaded successfully.");

        await loadDashboard();
        await loadTickets();
        await loadAnalytics();

        document.getElementById("upload-status").innerHTML = `

        <div class="sim-success">

            <h3>✅ Dataset Uploaded Successfully</h3>

            <p>

                Imported

                <strong>${result.ticketsImported}</strong>

                tickets.

            </p>

            <p>

                Duplicates Skipped

                <strong>${result.duplicatesSkipped}</strong>

            </p>

        </div>

        `;

        showNotification(
            "Dataset uploaded successfully."
        );

    }

    catch(error){

        console.error(error);

    }

}

// =======================================================
// VALIDATE DATASET
// =======================================================

document.getElementById(

    "btn-validate"

)?.addEventListener(

    "click",

    validateDataset

);

async function validateDataset(){

    try{

        const response = await fetch(

            API_BASE +

            "/ingestion/validate",

            {

                method:"POST"

            }

        );

        const result = await response.json();

        openModal(

            JSON.stringify(

                result,

                null,

                2

            )

        );

    }

    catch(error){

        console.error(error);

    }

}

// =======================================================
// REFRESH DASHBOARD
// =======================================================

async function refreshDashboard(){

    await heartbeat();

    await loadDashboard();

    await loadTickets();

    await loadAnalytics();

    addActivity("Dashboard Refreshed");

}

// =======================================================
// ACTIVITY FEED
// =======================================================

function addActivity(message){

    const feed=document.getElementById("activity-feed");

    if(!feed) return;

    const now=new Date().toLocaleTimeString();

    const div=document.createElement("div");

    div.className="activity-item";

    div.innerHTML=`

        <div class="activity-time">${now}</div>

        <div class="activity-text">${message}</div>

    `;

    feed.prepend(div);

    while(feed.children.length>20){

        feed.removeChild(feed.lastChild);

    }

}

function showNotification(message){

    const box = document.createElement("div");

    box.className = "live-notification";

    box.innerHTML = `
        🔔 ${message}
    `;

    document.body.appendChild(box);

    setTimeout(()=>{

        box.classList.add("show");

    },100);

    setTimeout(()=>{

        box.classList.remove("show");

        setTimeout(()=>{

            box.remove();

        },300);

    },3000);

}

// =======================================================
// MODAL
// =======================================================

function openModal(message){

    document.getElementById(

        "modal-content"

    ).innerHTML =

    message;

    document.getElementById(

        "modal"

    ).classList.add(

        "active"

    );

}

function closeModal(){

    document.getElementById(

        "modal"

    ).classList.remove(

        "active"

    );

}

function animateWorkflow(){

    const agents=document.querySelectorAll(".agent-node");

    if(agents.length===0){
        return;
    }

    agents.forEach(agent=>{
        agent.classList.remove("agent-active");
    });

    let index = 0;

    const timer = setInterval(()=>{

        if(index>0){
            agents[index-1].classList.remove("agent-active");
            agents[index-1].classList.add("agent-complete");
        }

        if(index<agents.length){

            agents[index].classList.add("agent-active");

            index++;

        }
        else{

            clearInterval(timer);

        }

    },800);

}



function animateTraceTimeline(){

    const steps = document.querySelectorAll(".trace-step-card");

    if(!steps.length){
        return;
    }

    steps.forEach(step=>{

        step.style.opacity = "0";

        step.style.transform = "translateX(-20px)";

    });

    steps.forEach((step,index)=>{

        setTimeout(()=>{

            step.style.transition = "all .5s ease";

            step.style.opacity = "1";

            step.style.transform = "translateX(0)";

        }, index*500);

    });

}

// =======================================================
// HELPERS
// =======================================================

function formatText(text){

    if(!text) return "";

    return text
        .replaceAll("_"," ")
        .toLowerCase()
        .replace(/\b\w/g,c=>c.toUpperCase());

}

function setText(id,value){

    const element =

        document.getElementById(id);

    if(element){

        element.innerHTML = value;

    }

}

function animateMetric(id, value){

    const el = document.getElementById(id);

    if(!el) return;

    el.classList.remove("metric-update");

    void el.offsetWidth;

    el.innerHTML = value;

    el.classList.add("metric-update");

}

function getValue(id){

    const element =

        document.getElementById(id);

    if(!element){

        return "";

    }

    return element.value;

}

function clearElement(id){

    const element =

        document.getElementById(id);

    if(element){

        element.innerHTML = "";

    }

}

function formatDate(date){

    return new Date(date)

        .toLocaleString();

}

// =======================================================
// AUTO HEARTBEAT
// =======================================================

setInterval(()=>{

    if(document.visibilityState==="visible"){

        heartbeat();

    }

},30000);

// =======================================================
// OPTIONAL WEBSOCKET
// =======================================================

let socket;

function connectWebSocket(){

    socket = new WebSocket(
        "ws://127.0.0.1:8000/ws"
    );

    socket.onopen = () => {

        addActivity("WebSocket Connected");

        const health =
            document.getElementById("ai-health");

        if(health){

            health.innerHTML="🟢 Healthy";

            health.style.color="#22C55E";

        }

    };

    socket.onmessage = (event) => {

        const msg = JSON.parse(event.data);

        addActivity(
            "Realtime: " + msg.event
        );

    };

    socket.onclose = () => {

        addActivity("WebSocket Disconnected");

        const health =
            document.getElementById("ai-health");

        if(health){

            health.innerHTML="🔴 Offline";

            health.style.color="#EF4444";

        }

    };

}

function startLiveClock(){

    const clock=document.getElementById("live-clock");

    function update(){

        clock.innerHTML=
        new Date().toLocaleString();

    }

    update();

    setInterval(update,1000);

}

function showLoadingScreen(){

    const progress =
        document.getElementById(
            "loader-progress"
        );

    const screen =
        document.getElementById(
            "loading-screen"
        );

    if(!progress || !screen){
        return;
    }

    let value = 0;

    const timer = setInterval(()=>{

        value += 5;

        progress.style.width =
            value + "%";

        if(value >= 100){

            clearInterval(timer);

            setTimeout(()=>{

                screen.style.display = "none";

            },300);

        }

    },100);

}

function renderAIInsights(){

    if(!dashboardData){
        return;
    }

    const panel = document.getElementById("ai-insights");

    if(!panel){
        return;
    }

    const overview = dashboardData.overview;

    const categories = dashboardData.categories || [];

    const priorities = dashboardData.priorities || [];

    const topCategory =
        categories.length
            ? categories.sort((a,b)=>b.count-a.count)[0]
            : {
                category: "N/A",
                count: 0
            };

    const topPriority =
        priorities.length
            ? priorities.sort((a,b)=>b.count-a.count)[0]
            : {
                priority: "N/A",
                count: 0
            };

    panel.innerHTML = `

        <ul class="insight-list">

            <li>
                📊 Total Tickets:
                <strong>${overview.totalTicketsProcessed}</strong>
            </li>

            <li>
                🗂 Most Common Category:
                <strong>${topCategory.category}</strong>
                (${topCategory.count})
            </li>

            <li>
                ⚡ Most Common Priority:
                <strong>${topPriority.priority}</strong>
                (${topPriority.count})
            </li>

            <li>
                ✅ Resolution Rate:
                <strong>${overview.resolutionRate}%</strong>
            </li>

            <li>
                🛡 Blocked Threats:
                <strong>${overview.blockedThreats}</strong>
            </li>

        </ul>

    `;

}

async function exportReport(){

    const { jsPDF } = window.jspdf;

    const pdf = new jsPDF();

    const overview = dashboardData.overview;

    pdf.setFontSize(20);

    pdf.text(
        "Supportlytics AI Enterprise",
        20,
        20
    );

    pdf.setFontSize(12);

    pdf.text(
        "Dashboard Report",
        20,
        30
    );

    pdf.line(20,35,190,35);

    pdf.text(
        "Total Tickets : " +
        overview.totalTicketsProcessed,
        20,
        50
    );

    pdf.text(
        "Resolved : " +
        overview.autoResolved,
        20,
        60
    );

    pdf.text(
        "HITL Holds : " +
        overview.hitlHolds,
        20,
        70
    );

    pdf.text(
        "Blocked Threats : " +
        overview.blockedThreats,
        20,
        80
    );

    pdf.text(
        "Resolution Rate : " +
        overview.resolutionRate + "%",
        20,
        90
    );

    pdf.save(
        "Supportlytics_Report.pdf"
    );

    showNotification(
        "Dashboard report exported."
    );

}



// =======================================================
// END
// =======================================================

console.log(

"===================================="

);

console.log(

"Supportlytics AI Enterprise"

);

console.log(

"Frontend Loaded Successfully"

);

console.log(

"===================================="

);

