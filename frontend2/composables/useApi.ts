export function useApi() {
  // const baseURL = "";
  const baseURL = "http://127.0.0.1:8000";

  const loading = useState("loading");
  loading.value = false;
  const jwt = useCookie("jwt");
  const head = computed(() => {
    if (jwt.value) {
      return {
        Authorization: `Bearer ${jwt.value}`,
        Accept: "application/json",
      };
    } else {
      return {
        Accept: "application/json",
      };
    }
  });

  function endpointModify(endpoint: string) {
    const activeEcommerce = useCookie("ecommerce");
    const activeBlog = useCookie("blog");
    const activeWebsite = useCookie("website");
    if (activeEcommerce.value && endpoint.indexOf("/api/ecommerce/") !== -1) {
      if (endpoint.indexOf("?") !== -1) {
        endpoint = endpoint += "&ecommerce=" + activeEcommerce.value;
      } else {
        endpoint = endpoint += "?ecommerce=" + activeEcommerce.value;
      }
    } else if (activeBlog.value && endpoint.indexOf("/api/blog/") !== -1) {
      if (endpoint.indexOf("?") !== -1) {
        endpoint = endpoint += "&blog=" + activeBlog.value;
      } else {
        endpoint = endpoint += "?blog=" + activeBlog.value;
      }
    } else if (
      activeWebsite.value &&
      endpoint.indexOf("/api/website/") !== -1
    ) {
      if (endpoint.indexOf("?") !== -1) {
        endpoint = endpoint += "&website=" + activeWebsite.value;
      } else {
        endpoint = endpoint += "?website=" + activeWebsite.value;
      }
    }

    return endpoint;
  }

  const get = async (endpoint: string) => {
    endpoint = endpointModify(endpoint);
    loading.value = true;
    const { data, pending, error, refresh } = await useFetch<any>(
      baseURL + endpoint,
      {
        headers: head.value,
        method: "get",
      }
    );
    loading.value = false;
    if (typeof data.value === "object" && "navigate" in data?.value) {
      navigateTo(data.value.navigate);
    }
    return {
      data: data.value,
      error: error.value,
    };
  };
  const post = async (endpoint: string, postdata: object) => {
    endpoint = endpointModify(endpoint);
    loading.value = true;
    const { data, pending, error, refresh } = await useFetch<any>(
      baseURL + endpoint,
      {
        headers: head.value,
        method: "post",
        body: JSON.stringify(postdata),
      }
    );
    loading.value = false;
    return {
      data: data.value,
      error: error.value,
    };
  };

  const put = async (endpoint: string, postdata: object) => {
    endpoint = endpointModify(endpoint);
    loading.value = true;
    const { data, pending, error, refresh } = await useFetch<any>(
      baseURL + endpoint,
      {
        headers: head.value,
        method: "put",
        body: JSON.stringify(postdata),
      }
    );
    loading.value = false;
    return {
      data: data.value,
      error: error.value,
    };
  };

  const del = async (endpoint: string) => {
    endpoint = endpointModify(endpoint);
    loading.value = true;
    const { data, pending, error, refresh } = await useFetch<any>(
      baseURL + endpoint,
      {
        headers: head.value,
        method: "delete",
      }
    );
    loading.value = false;
    return {
      data: data.value,
      error: error.value,
    };
  };

  const Api = {
    baseURL,
    get: get,
    post: post,
    put: put,
    del: del,
  };

  return Api;
}
