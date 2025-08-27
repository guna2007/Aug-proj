document.addEventListener("DOMContentLoaded", () => {
  const animatedElements = document.querySelectorAll(".plot-card");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    {
      rootMargin: "0px",
      threshold: 0.1,
    }
  );
  animatedElements.forEach((el) => observer.observe(el));

  // Modal logic for plot details
  const plotSummaries = {
    delay_correlations: {
      title: "Delay Correlations",
      img: "graphs/basic_plots/delay_correlations.png",
      summary: `This plot explores how delivery delays are related to other order features such as payment type, product category, and seller. By visualizing these correlations, it helps identify which factors most strongly contribute to late deliveries. Business teams can use these insights to prioritize process improvements and target interventions where they will have the greatest impact.`,
    },
    delivery_time_distribution: {
      title: "Delivery Time Distribution",
      img: "graphs/basic_plots/delivery_time_distribution.png",
      summary: `This visualization shows the distribution of delivery times across all orders. Most deliveries fall within a predictable window, but the presence of outliers highlights occasional inefficiencies. Understanding this spread helps set realistic customer expectations and guides efforts to reduce extreme delays.`,
    },
    late_rate: {
      title: "Late Delivery Rate",
      img: "graphs/basic_plots/late_rate.png",
      summary: `This chart displays the percentage of orders delivered late. It quantifies operational bottlenecks and highlights periods or processes where delays are most frequent. Monitoring this rate is crucial for tracking service level improvements and maintaining customer satisfaction.`,
    },
    review_distribution: {
      title: "Review Score Distribution",
      img: "graphs/basic_plots/review_distribution.png",
      summary: `Customer review scores are visualized here, providing a snapshot of overall satisfaction. Peaks at high scores indicate strong performance, while lower scores point to areas needing attention. This plot helps prioritize quality improvements and customer support initiatives.`,
    },
    top_categories: {
      title: "Top Product Categories",
      img: "graphs/basic_plots/top_categories.png",
      summary: `This plot highlights the most popular product categories by order volume. It guides inventory management, marketing strategies, and helps identify growth opportunities. Focusing on top categories ensures resources are allocated efficiently to meet demand.`,
    },
    eda_delay_by_seller: {
      title: "Delay by Seller",
      img: "graphs/business/eda_delay_by_seller.png",
      summary: `This visualization identifies sellers with frequent delivery delays. By pinpointing problematic vendors, it enables targeted vendor management and supports negotiations for improved service levels. Reducing seller-related delays directly enhances customer experience.`,
    },
    eda_delay_by_state: {
      title: "Delay by State",
      img: "graphs/business/eda_delay_by_state.png",
      summary: `Delivery delays are mapped by state, revealing regional logistics challenges. This helps optimize shipping routes, allocate resources, and address state-specific issues. Businesses can use this insight to improve delivery performance in underperforming regions.`,
    },
    eda_late_by_category: {
      title: "Late Rate by Category",
      img: "graphs/business/eda_late_by_category.png",
      summary: `This plot shows which product categories have the highest rates of late delivery. It informs supply chain improvements and helps prioritize efforts for categories most affected by delays. Addressing these issues can boost customer satisfaction and retention.`,
    },
    eda_late_by_payment: {
      title: "Late Rate by Payment Type",
      img: "graphs/business/eda_late_by_payment.png",
      summary: `Late deliveries are analyzed by payment method, uncovering potential process inefficiencies. Certain payment types may be linked to longer processing times or increased risk of delay. This insight supports process optimization and policy adjustments.`,
    },
    eda_monthly_trend: {
      title: "Monthly Order & Delay Trend",
      img: "graphs/business/eda_monthly_trend.png",
      summary: `This time series tracks order volume and delivery delays month by month. It reveals seasonal patterns, growth trends, and periods of operational stress. Understanding these trends helps with forecasting, staffing, and strategic planning.`,
    },
  };

  const modal = document.getElementById("plotModal");
  const closeModalBtn = document.getElementById("closeModal");
  const modalPlotImg = document.getElementById("modalPlotImg");
  const modalPlotTitle = document.getElementById("modalPlotTitle");
  const modalPlotSummary = document.getElementById("modalPlotSummary");

  document.querySelectorAll(".plot-card").forEach((card) => {
    card.addEventListener("click", () => {
      const plotKey = card.getAttribute("data-plot");
      const plotInfo = plotSummaries[plotKey];
      if (plotInfo) {
        modalPlotImg.src = plotInfo.img;
        modalPlotImg.alt = plotInfo.title;
        modalPlotTitle.textContent = plotInfo.title;
        modalPlotSummary.textContent = plotInfo.summary;
        modal.style.display = "block";
        document.body.style.overflow = "hidden";
      }
    });
  });

  closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  });

  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    }
  });
});
