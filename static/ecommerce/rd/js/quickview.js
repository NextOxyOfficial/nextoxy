createApp({
  data() {
    return {
      product: "",
      variations: "",
    };
  },
  delimiters: ["[[", "]]"],
  mounted() {
    this.getProduct(localStorage.getItem("quick-view"));
  },
  methods: {
    getProduct(id) {
      console.log(id);
      fetch("/api/detail?id=" + id, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          this.product = data;
          this.variations = data.variations;
          this.$nextTick(() => {
            $(".owl-carousel").owlCarousel({
              items: 1,
            });
          });
        })
        .catch((error) => console.error(error));
    },
  },
}).mount("#quick-view");
