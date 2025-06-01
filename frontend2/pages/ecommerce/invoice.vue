<script setup>
    definePageMeta({
        layout: 'blank'
    })
    const {shop}= useShop()
    const route = useRoute()
    const Api = useApi()
    const order = ref('')
    async function getOrder(){
        const response = await Api.get('/api/ecommerce/dash/orders?oid='+route.query.oid)
        order.value = response.data
        console.log(order.value);
    }
    onMounted(() => {
        getOrder()
    })
    
    const printInvoice = () => {
        var actions = document.getElementById('actions')
        actions.style.display = 'none'
        window.print();
        setTimeout(() => {
            actions.style.display = 'flex'
        }, 500);
    }
    console.log(777)
</script>
<template>
    <section id="invoice" class="my-2" v-if="shop && order">
        <div class="flex justify-center gap-1 w-full my-5" id="actions">
            <button class="px-3 py-1" @click="printInvoice">Print</button>
            <NuxtLink to="/ecommerce/orders" class="px-3 py-1 cursor-pointer rounded bg-slate-100">Close</NuxtLink>
        </div>
        <table width="100%" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#e1e1e1">
          <tr>
            <td height="20"></td>
          </tr>
          <tr>
            <td>
              <table width="600" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#ffffff" style="border-radius: 10px 10px 0 0;">
                <tr class="hiddenMobile">
                  <td height="40"></td>
                </tr>
                <tr class="visibleMobile">
                  <td height="30"></td>
                </tr>
        
                <tr>
                  <td>
                    <table width="480" border="0" cellpadding="0" cellspacing="0" align="center" class="fullPadding">
                      <tbody>
                        <tr>
                          <td>
                            <table width="220" border="0" cellpadding="0" cellspacing="0" align="left" class="col">
                              <tbody>
                                <tr>
                                  <td align="left"> 
                                    <img v-if="shop.logo" :src="Api.baseURL + shop.logo" style="max-height: 50px;" alt="logo" border="0" />
                                    <img v-else :src="Api.baseURL + '/static/ecommerce/logo.png'" style="max-height: 50px;" alt="logo" border="0" />
                                  </td>
                                </tr>
                                <tr class="hiddenMobile">
                                  <td height="40"></td>
                                </tr>
                                <tr class="visibleMobile">
                                  <td height="20"></td>
                                </tr>
                                <tr>
                                  <td style="font-size: 12px; color: #5b5b5b; font-family: 'Open Sans', sans-serif; line-height: 18px; vertical-align: top; text-align: left;">
                                    Hello, {{ order.address.first_name }} {{ order.address.last_name }}.
                                    <br> Thank you for shopping from our store and for your order.
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table width="220" border="0" cellpadding="0" cellspacing="0" align="right" class="col">
                              <tbody>
                                <tr class="visibleMobile">
                                  <td height="20"></td>
                                </tr>
                                <tr>
                                  <td height="5"></td>
                                </tr>
                                <tr>
                                  <td style="font-size: 21px; color: #ff0000; letter-spacing: -1px; font-family: 'Open Sans', sans-serif; line-height: 1; vertical-align: top; text-align: right;">
                                    Invoice
                                  </td>
                                </tr>
                                <tr class="hiddenMobile">
                                  <td height="50"></td>
                                </tr>
                                <tr class="visibleMobile">
                                  <td height="20"></td>
                                </tr>
                                <tr>
                                  <td style="font-size: 12px; color: #5b5b5b; font-family: 'Open Sans', sans-serif; line-height: 18px; vertical-align: top; text-align: right;">
                                    <small>ORDER</small> #{{ order.id }}<br />
                                    <small>{{ order.created_at }}</small>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
        <!-- /Header -->
        <!-- Order Details -->
        <table width="100%" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#e1e1e1">
          <tbody>
            <tr>
              <td>
                <table width="600" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#ffffff">
                  <tbody>
                    <tr class="hiddenMobile">
                      <td height="60"></td>
                    </tr>
                    <tr class="visibleMobile">
                      <td height="40"></td>
                    </tr>
                    <tr>
                      <td>
                        <table width="480" border="0" cellpadding="0" cellspacing="0" align="center" class="fullPadding">
                          <tbody>
                            <tr>
                              <th style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #5b5b5b; font-weight: normal; line-height: 1; vertical-align: top; padding: 0 10px 7px 0;" width="52%" align="left">
                                Item
                              </th>
                              <th style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #5b5b5b; font-weight: normal; line-height: 1; vertical-align: top; padding: 0 0 7px;" align="left">
                                <small>ID</small>
                              </th>
                              <th style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #5b5b5b; font-weight: normal; line-height: 1; vertical-align: top; padding: 0 0 7px;" align="center">
                                Quantity
                              </th>
                              <th style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #1e2b33; font-weight: normal; line-height: 1; vertical-align: top; padding: 0 0 7px;" align="right">
                                Subtotal
                              </th>
                            </tr>
                            <tr>
                              <td height="1" style="background: #bebebe;" colspan="4"></td>
                            </tr>
                            <template v-for="item in order.items">
                                <tr>
                                    <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #ff0000;  line-height: 18px;  vertical-align: top; padding:7px 0;" class="article">
                                    {{item.name}}
                                    </td>
                                    <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #646a6e;  line-height: 18px;  vertical-align: top; padding:7px 0;">
                                        <small>{{item.id}}</small>
                                    </td>
                                    <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #646a6e;  line-height: 18px;  vertical-align: top; padding:7px 0;" align="center">
                                        {{ item.quantity }}
                                    </td>
                                    <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #1e2b33;  line-height: 18px;  vertical-align: top; padding:7px 0;" align="right">
                                        {{shop.currency}} {{ item.sale_price * item.quantity }}
                                    </td>
                                </tr>
                                <tr>
                                    <td height="1" colspan="4" style="border-bottom:1px solid #e4e4e4"></td>
                                </tr>
                            </template>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td height="20"></td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- /Order Details -->
        <!-- Total -->
        <table width="100%" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#e1e1e1">
          <tbody>
            <tr>
              <td>
                <table width="600" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#ffffff">
                  <tbody>
                    <tr>
                      <td>
        
                        <!-- Table Total -->
                        <table width="480" border="0" cellpadding="0" cellspacing="0" align="center" class="fullPadding">
                          <tbody>
                            <tr>
                              <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #646a6e; line-height: 22px; vertical-align: top; text-align:right; ">
                                Subtotal
                              </td>
                              <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #646a6e; line-height: 22px; vertical-align: top; text-align:right; white-space:nowrap;" width="80">
                                {{shop.currency}} {{ order.subtotal }}
                              </td>
                            </tr>
                            <tr>
                              <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #646a6e; line-height: 22px; vertical-align: top; text-align:right; ">
                                Shipping &amp; Handling
                              </td>
                              <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #646a6e; line-height: 22px; vertical-align: top; text-align:right; ">
                                {{shop.currency}} {{ order.shipping }}
                              </td>
                            </tr>
                            <tr>
                              <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #000; line-height: 22px; vertical-align: top; text-align:right; ">
                                <strong>Grand Total (Incl.Tax)</strong>
                              </td>
                              <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #000; line-height: 22px; vertical-align: top; text-align:right; ">
                                <strong>{{shop.currency}} {{ order.total }}</strong>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <!-- /Table Total -->
        
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- /Total -->
        <!-- Information -->
        <table width="100%" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#e1e1e1">
          <tbody>
            <tr>
              <td>
                <table width="600" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#ffffff">
                  <tbody>
                    <tr class="hiddenMobile">
                      <td height="60"></td>
                    </tr>
                    <tr class="visibleMobile">
                      <td height="40"></td>
                    </tr>
                    <tr>
                      <td>
                        <table width="480" border="0" cellpadding="0" cellspacing="0" align="center" class="fullPadding">
                          <tbody>
                            <tr style="text-align: center;">
                              <td>
                                <table width="220" border="0" cellpadding="0" cellspacing="0" align="left" class="col">
        
                                  <tbody>
                                    <tr>
                                      <td style="font-size: 11px; font-family: 'Open Sans', sans-serif; color: #5b5b5b; line-height: 1; vertical-align: top; ">
                                        <strong>BILLING INFORMATION</strong>
                                      </td>
                                    </tr>
                                    <tr>
                                      <td width="100%" height="10"></td>
                                    </tr>
                                    <tr>
                                      <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #5b5b5b; line-height: 20px; vertical-align: top; ">
                                        {{ order.address.first_name }} {{ order.address.last_name }}<br> 
                                        {{ order.address.street_address }}<br>
                                        {{ order.address.city }}, {{ order.address.state }}, {{ order.address.country }}<br>
                                        {{ order.address.phone }}<br>
                                        {{ order.address.email }}
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                               </td>
                               <td>
                                <table width="220" border="0" cellpadding="0" cellspacing="0" align="left" class="col">
                                    <tbody>
                                    <tr class="visibleMobile">
                                        <td height="20"></td>
                                    </tr>
                                    <tr>
                                        <td style="font-size: 11px; font-family: 'Open Sans', sans-serif; color: #5b5b5b; line-height: 1; vertical-align: top; ">
                                        <strong>SHIPPING INFORMATION</strong>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td width="100%" height="10"></td>
                                    </tr>
                                    <tr>
                                        <td style="font-size: 12px; font-family: 'Open Sans', sans-serif; color: #5b5b5b; line-height: 20px; vertical-align: top; ">
                                            {{ order.address.first_name }} {{ order.address.last_name }}<br> 
                                            {{ order.address.street_address }}<br>
                                            {{ order.address.city }}, {{ order.address.state }}, {{ order.address.country }}<br>
                                            {{ order.address.phone }}<br>
                                            {{ order.address.email }}
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                
                
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td>
                      </td>
                    </tr>
                    <tr class="hiddenMobile">
                      <td height="60"></td>
                    </tr>
                    <tr class="visibleMobile">
                      <td height="30"></td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
        <table width="100%" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#e1e1e1">
            <tr>
            <td>
                <table width="600" border="0" cellpadding="0" cellspacing="0" align="center" class="fullTable" bgcolor="#ffffff" style="border-radius: 0 0 10px 10px;">
                <tr>
                    <td>
                    <table width="480" border="0" cellpadding="0" cellspacing="0" align="center" class="fullPadding">
                        <tbody>
                        <tr>
                            <td style="font-size: 12px; color: #5b5b5b; font-family: 'Open Sans', sans-serif; line-height: 18px; vertical-align: top; text-align: left;">
                            Have a nice day.
                            </td>
                            <td style="font-size: 12px; color: #5b5b5b; font-family: 'Open Sans', sans-serif; line-height: 18px; vertical-align: top; text-align: left;">
                              <b>{{ shop.name }}</b> {{ shop.address }}, {{ shop.city }}, {{ shop.state }}, {{ shop.country }} | {{ shop.phone }}, {{ shop.email }}
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </td>
                </tr>
                <tr class="spacer">
                    <td height="50"></td>
                </tr>
    
                </table>
            </td>
            </tr>
            <tr>
            <td height="20"></td>
            </tr>
        </table>
    </section>
    </template>
    
    
    <style scoped>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700);
      body { margin: 0; padding: 0; background: #e1e1e1; }
      div, p, a, li, td { -webkit-text-size-adjust: none; }
      .ReadMsgBody { width: 100%; background-color: #ffffff; }
      .ExternalClass { width: 100%; background-color: #ffffff; }
      body { width: 100%; height: 100%; background-color: #e1e1e1; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
      html { width: 100%; }
      p { padding: 0 !important; margin-top: 0 !important; margin-right: 0 !important; margin-bottom: 0 !important; margin-left: 0 !important; }
      .visibleMobile { display: none; }
      .hiddenMobile { display: block; }
    
      @media only screen and (max-width: 600px) {
      body { width: auto !important; }
      table[class=fullTable] { width: 96% !important; clear: both; }
      table[class=fullPadding] { width: 85% !important; clear: both; }
      table[class=col] { width: 45% !important; }
      .erase { display: none; }
      }
    
      @media only screen and (max-width: 420px) {
      table[class=fullTable] { width: 100% !important; clear: both; }
      table[class=fullPadding] { width: 85% !important; clear: both; }
      table[class=col] { width: 100% !important; clear: both; }
      table[class=col] td { text-align: left !important; }
      .erase { display: none; font-size: 0; max-height: 0; line-height: 0; padding: 0; }
      .visibleMobile { display: block !important; }
      .hiddenMobile { display: none !important; }
      }
    </style>