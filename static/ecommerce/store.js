const store = Vuex.createStore({
    state() {
      const cart = localStorage.getItem('cart') || '[]';
      const wish = localStorage.getItem('wish') || '[]';
      return {
        cart: JSON.parse(cart),
        wish: JSON.parse(wish),
      }
    },
    mutations: {
      // cart 
      addToCart(state, product) {
        console.log(product);
        const index = state.cart.findIndex(
          (item) => item.id === product.id
        )
        if (index !== -1) {
          state.cart[index].quantity += product.quantity
        } else {
          state.cart.push(product)
        }
        localStorage.setItem('cart', JSON.stringify(state.cart))
      },
      removeFromCart(state, product) {
        const index = state.cart.findIndex(
          (item) => item.id === product.id
        )
        console.log(index)
        if (index !== -1) {
          state.cart.splice(index, 1)
        }
        localStorage.setItem('cart', JSON.stringify(state.cart))
      },
      // wish 
      addToWish(state, product) {
        const index = state.wish.findIndex(
          (item) => item.id === product.id
        )
        if (index === -1) {
          state.wish.push(product)
        }
        localStorage.setItem('wish', JSON.stringify(state.wish))
      },
      removeFromWish(state, product) {
        const index = state.wish.findIndex(
          (item) => item.id === product.id
        )
        if (index !== -1) {
          state.wish.splice(index, 1)
        }
        localStorage.setItem('wish', JSON.stringify(state.wish))
      },
    }
  })