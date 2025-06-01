export function useShop() {
    const Api = useApi()
    const shop = useState<any>('shop', ()=>null)
    
    const getShop = async () => {
        const res = await Api.get('/api/ecommerce/dash/shop')
            if (res.data) {
            shop.value = res.data
        }
    }
    return { shop, getShop }
}