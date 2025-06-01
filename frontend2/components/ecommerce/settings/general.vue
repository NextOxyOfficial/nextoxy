<template>
  <div>
    <div class="space-y-6 sm:px-6 lg:col-span-9 lg:px-0 mt-4">
      <!-- Plan -->
      <BaseCard shape="rounded" aria-labelledby="plan-heading">
        <form>
          <div class="sm:overflow-hidden sm:rounded-md">
            <div shape="rounded" class="p-4">
              <h2
                id="payment-details-heading"
                class="text-lg font-medium leading-6"
              >
                <Icon
                  name="ph:gear-fine-duotone"
                  class="inline h-9 w-9 mr-2 text-primary-500 p-2 border border-primary-800/30 bg-primary-600/10 rounded-full"
                />
                Logo & Images
              </h2>
              <p class="mt-1 text-sm text-gray-500 pl-12">
                Please note that updating your location could take few minutes
                to take effect.
              </p>
            </div>
            <div
              class="bg-white/10 py-6 px-4 sm:p-6 flex gap-2 items-start justify-start whitespace-nowrap flex-wrap"
            >
              <div class="flex-1 relative w-1/2 md:min-w-[100px]">
                <label for="" class="block text-sm font-medium text-center mb-2"
                  >Main logo</label
                >
                <div
                  class="flex w-full items-center justify-start bg-grey-lighter"
                >
                  <img
                    :src="shop.newLogo"
                    alt=""
                    srcset=""
                    class="h-28 max-w-full my-2 object-contain rounded border-gray-200/10"
                    v-if="shop.newLogo"
                  />
                  <img
                    :src="Api.baseURL + shop.logo"
                    alt=""
                    srcset=""
                    class="h-28 max-w-full my-2 object-contain rounded w-28 border border-slate-500/20"
                    v-else-if="shop.logo"
                  />
                  <label
                    :class="{ 'absolute opacity-0': shop.newLogo || shop.logo }"
                    class="w-56 h-28 flex flex-col items-center px-2 py-4 bg-white/10 text-purple-500 rounded tracking-wide uppercase border border-blue cursor-pointer hover:bg-blue hover:border-gray-200/10"
                  >
                    <svg
                      class="w-8 h-8"
                      fill="currentColor"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                    >
                      <path
                        d="M16.88 9.1A4 4 0 0 1 16 17H5a5 5 0 0 1-1-9.9V7a3 3 0 0 1 4.52-2.59A4.98 4.98 0 0 1 17 8c0 .38-.04.74-.12 1.1zM11 11h3l-4-4-4 4h3v3h2v-3z"
                      />
                    </svg>
                    <span class="mt-2 text-base leading-normal"
                      >Upload Logo</span
                    >
                    <input @change="logoUploaded" type="file" class="hidden" />
                  </label>
                </div>
                <p
                  class="text-xs flex items-center gap-1"
                  v-if="shop.newLogo || shop.logo"
                >
                  <Icon name="ph:paperclip" />
                  Click To Change
                </p>
              </div>
              <div class="flex-1 w-1/2 md:w-[100px]">
                <label for="" class="block text-sm font-medium text-center mb-2"
                  >Favicon</label
                >
                <div
                  class="flex w-full items-center justify-start bg-grey-lighter"
                >
                  <img
                    :src="shop.newFavicon"
                    alt=""
                    srcset=""
                    class="h-28 max-w-full my-2 object-contain rounded"
                    v-if="shop.newFavicon"
                  />
                  <img
                    :src="Api.baseURL + shop.favicon"
                    alt=""
                    srcset=""
                    class="h-28 max-w-full my-2 object-contain rounded w-28 border border-slate-500/20"
                    v-else-if="shop.favicon"
                  />
                  <label
                    :class="{
                      'absolute opacity-0': shop.newFavicon || shop.favicon,
                    }"
                    class="w-56 h-28 flex flex-col items-center px-2 py-4 bg-white/10 text-purple-500 rounded tracking-wide uppercase border border-slate-700/10 cursor-pointer hover:bg-blue hover:border-gray-200/10"
                  >
                    <svg
                      class="w-8 h-8"
                      fill="currentColor"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                    >
                      <path
                        d="M16.88 9.1A4 4 0 0 1 16 17H5a5 5 0 0 1-1-9.9V7a3 3 0 0 1 4.52-2.59A4.98 4.98 0 0 1 17 8c0 .38-.04.74-.12 1.1zM11 11h3l-4-4-4 4h3v3h2v-3z"
                      />
                    </svg>
                    <span class="mt-2 text-base leading-normal"
                      >Upload Favicon</span
                    >
                    <input @change="favUploaded" type="file" class="hidden" />
                  </label>
                </div>
                <p
                  class="text-xs flex items-center gap-1"
                  v-if="shop.newFavicon || shop.favicon"
                >
                  <Icon name="ph:paperclip" />
                  Click To Change
                </p>
              </div>
              <div class="flex-1 w-1/2 md:w-[100px]">
                <label for="" class="block text-sm font-medium text-center mb-2"
                  >Payment Gateway</label
                >
                <div
                  class="flex w-full items-center justify-start bg-grey-lighter"
                >
                  <img
                    :src="shop.newPayment_image"
                    alt=""
                    srcset=""
                    class="h-28 max-w-full my-2 object-contain rounded"
                    v-if="shop.newPayment_image"
                  />
                  <img
                    :src="Api.baseURL + shop.payment_image"
                    alt=""
                    srcset=""
                    class="h-28 max-w-full my-2 object-contain rounded w-28 border border-slate-500/20"
                    v-else-if="shop.payment_image"
                  />
                  <label
                    :class="{
                      'absolute opacity-0': shop.newFavicon || shop.favicon,
                    }"
                    class="w-56 h-28 flex flex-col items-center px-2 py-4 bg-white/10 text-purple-500 rounded tracking-wide uppercase border border-slate-700/10 cursor-pointer hover:bg-blue hover:border-gray-200/10"
                  >
                    <svg
                      class="w-8 h-8"
                      fill="currentColor"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                    >
                      <path
                        d="M16.88 9.1A4 4 0 0 1 16 17H5a5 5 0 0 1-1-9.9V7a3 3 0 0 1 4.52-2.59A4.98 4.98 0 0 1 17 8c0 .38-.04.74-.12 1.1zM11 11h3l-4-4-4 4h3v3h2v-3z"
                      />
                    </svg>
                    <span class="mt-2 text-base leading-normal"
                      >Upload Image</span
                    >
                    <input
                      @change="paymentLogosUploaded"
                      type="file"
                      class="hidden"
                    />
                  </label>
                </div>
                <p
                  class="text-xs flex items-center gap-1"
                  v-if="shop.newPayment_image || shop.payment_image"
                >
                  <Icon name="ph:paperclip" />
                  Click To Change
                </p>
              </div>
            </div>
          </div>
        </form>
      </BaseCard>
      <section aria-labelledby="payment-details-heading">
        <BaseCard shape="rounded" method="POST">
          <div class="sm:overflow-hidden sm:rounded-md">
            <div class="bg-white/10 py-6 px-4 sm:p-6">
              <div shape="rounded">
                <h2
                  id="payment-details-heading"
                  class="text-lg font-medium leading-6"
                >
                  <Icon
                    name="ph:gear-fine-duotone"
                    class="inline h-9 w-9 mr-2 text-primary-500 p-2 border border-primary-800/30 bg-primary-600/10 rounded-full"
                  />
                  Shop Settings
                </h2>
                <p class="mt-1 text-sm text-gray-500 dark:text-slate-300 pl-12">
                  Please note that updating your location could take few minutes
                  to take effect.
                </p>
              </div>
              <div class="mt-6 mb-10 grid grid-col-2 md:grid-cols-7 gap-6">
                <div class="col-span-1 md:col-span-5">
                  <label for="email-address" class="block text-sm font-medium"
                    >Site Title</label
                  >
                  <input
                    v-model="shop.title"
                    type="text"
                    name="email-address"
                    id="email-address"
                    autocomplete="email"
                    placeholder="Welcome to my store!"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>

                <div class="col-span-1 sm:col-span-2">
                  <label for="country" class="block text-sm font-medium"
                    >Currency</label
                  >
                  <select
                    v-model="shop.currency"
                    id="country"
                    name="country"
                    autocomplete="country-name"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm dark:text-gray-500 focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  >
                    <option value="">Auto Currency</option>
                    <option value="USD $">United States dollar - USD $</option>
                    <option value="GBP £">United Kingdom pound - GBP £</option>
                    <option value="AED د.إ">
                      United Arab Emirates dirham - AED د.إ
                    </option>
                    <option value="AFN ؋">Afghan afghani - AFN ؋</option>
                    <option value="ALL L">Albanian lek - ALL L</option>
                    <option value="AMD ֏">Armenian dram - AMD ֏</option>
                    <option value="ANG ƒ">
                      Netherlands Antillean guilder - ANG ƒ
                    </option>
                    <option value="AOA Kz">Angolan kwanza - AOA Kz</option>
                    <option value="ARS $">Argentine peso - ARS $</option>
                    <option value="AUD $">Australian dollar - AUD $</option>
                    <option value="AWG ƒ">Aruban florin - AWG ƒ</option>
                    <option value="AZN ₼">Azerbaijani manat - AZN ₼</option>
                    <option value="BBD $">Barbadian dollar - BBD $</option>
                    <option value="BDT ৳">Bangladeshi taka - BDT ৳</option>
                    <option value="BGN лв">Bulgarian lev - BGN лв</option>
                    <option value="BHD د.ب">Bahraini dinar - BHD د.ب</option>
                    <option value="BIF FBu">Burundian franc - BIF FBu</option>
                    <option value="BMD $">Bermudian dollar - BMD $</option>
                    <option value="BND $">Brunei dollar - BND $</option>
                    <option value="BOB $b">Bolivian boliviano - BOB $b</option>
                    <option value="BRL $">Brazilian real - BRL $</option>
                    <option value="BSD $">Bahamian dollar - BSD $</option>
                    <option value="BTN Nu.">
                      Bhutanese ngultrum - BTN Nu.
                    </option>
                    <option value="BWP P">Botswana pula - BWP P</option>
                    <option value="BYR Br">Belarusian ruble - BYR Br</option>
                    <option value="BZD $">Belize dollar - BZD $</option>
                    <option value="CAD $">Canadian dollar - CAD $</option>
                    <option value="CDF FC">Congolese franc - CDF FC</option>
                    <option value="CHE ₾">WIR Euro - CHE ₾</option>
                    <option value="CHF ₾">Swiss franc - CHF ₾</option>
                    <option value="CHW ₾">WIR Franc - CHW ₾</option>
                    <option value="CLP $">Chilean peso - CLP $</option>
                    <option value="CNY ¥">Chinese yuan - CNY ¥</option>
                    <option value="COP $">Colombian peso - COP $</option>
                    <option value="CRC ₡">Costa Rican colón - CRC ₡</option>
                    <option value="CUP $">Cuban peso - CUP $</option>
                    <option value="CVE $">Cape Verdean escudo - CVE $</option>
                    <option value="CZK Kč">Czech koruna - CZK Kč</option>
                    <option value="DJF Fdj">Djiboutian franc - DJF Fdj</option>
                    <option value="DKK kr">Danish krone - DKK kr</option>
                    <option value="DOP $">Dominican peso - DOP $</option>
                    <option value="DZD د.ج">Algerian dinar - DZD د.ج</option>
                    <option value="EGP £">Egyptian pound - EGP £</option>
                    <option value="ERN Nfk">Eritrean nakfa - ERN Nfk</option>
                    <option value="ETB Br">Ethiopian birr - ETB Br</option>
                    <option value="EUR €">European Euro - EUR €</option>
                    <option value="FJD $">Fijian dollar - FJD $</option>
                    <option value="GBP £">Pound sterling - GBP £</option>
                    <option value="GEL ₾">Georgian lari - GEL ₾</option>
                    <option value="GGP £">Guernsey pound - GGP £</option>
                    <option value="GHS ¢">Ghana cedi - GHS ¢</option>
                    <option value="GIP £">Gibraltar pound - GIP £</option>
                    <option value="GMD D">Gambian dalasi - GMD D</option>
                    <option value="GNF FG">Guinean franc - GNF FG</option>
                    <option value="GTQ Q">Guatemalan quetzal - GTQ Q</option>
                    <option value="GYD $">Guyanaese dollar - GYD $</option>
                    <option value="HKD $">Hong Kong dollar - HKD $</option>
                    <option value="HNL L">Honduran lempira - HNL L</option>
                    <option value="HRK kn">Croatian kuna - HRK kn</option>
                    <option value="HTG G">Haitian gourde - HTG G</option>
                    <option value="HUF Ft">Hungarian forint - HUF Ft</option>
                    <option value="IDR Rp">Indonesian rupiah - IDR Rp</option>
                    <option value="ILS ₪">Israeli new shekel - ILS ₪</option>
                    <option value="IMP £">Manx pound - IMP £</option>
                    <option value="INR ₹">Indian rupee - INR ₹</option>
                    <option value="IQD ع.د">Iraqi dinar - IQD ع.د</option>
                    <option value="IRR ریال">Iranian rial - IRR ریال</option>
                    <option value="ISK kr">Icelandic króna - ISK kr</option>
                    <option value="JEP £">Jersey pound - JEP £</option>
                    <option value="JMD $">Jamaican dollar - JMD $</option>
                    <option value="JOD د.ا">Jordanian dinar - JOD د.ا</option>
                    <option value="JPY ¥">Japanese yen - JPY ¥</option>
                    <option value="KES Sh">Kenyan shilling - KES Sh</option>
                    <option value="KGS лв">Kyrgyzstani som - KGS лв</option>
                    <option value="KHR ៛">Cambodian riel - KHR ៛</option>
                    <option value="KMF KM">Comorian franc - KMF KM</option>
                    <option value="KPW ₩">North Korean won - KPW ₩</option>
                    <option value="KRW ₩">South Korean won - KRW ₩</option>
                    <option value="KWD د.ك">Kuwaiti dinar - KWD د.ك</option>
                    <option value="KYD $">Cayman Islands dollar - KYD $</option>
                    <option value="KZT ₸">Kazakhstani tenge - KZT ₸</option>
                    <option value="LAK ₭">Lao kip - LAK ₭</option>
                    <option value="LBP ل.ل">Lebanese pound - LBP ل.ل</option>
                    <option value="LKR Rs">Sri Lankan rupee - LKR Rs</option>
                    <option value="LRD $">Liberian dollar - LRD $</option>
                    <option value="LSL L">Lesotho loti - LSL L</option>
                    <option value="LYD د.ل">Libyan dinar - LYD د.ل</option>
                    <option value="MAD د.م.">Moroccan dirham - MAD د.م.</option>
                    <option value="MDL L">Moldovan leu - MDL L</option>
                    <option value="MGA Ar">Malagasy ariary - MGA Ar</option>
                    <option value="MKD ден">Macedonian denar - MKD ден</option>
                    <option value="MMK K">Burmese kyat - MMK K</option>
                    <option value="MNT ₮">Mongolian tögrög - MNT ₮</option>
                    <option value="MOP MOP$">Macanese pataca - MOP MOP$</option>
                    <option value="MRU UM">Mauritanian ouguiya - MRU UM</option>
                    <option value="MUR Rs">Mauritian rupee - MUR Rs</option>
                    <option value="MVR Rf">Maldivian rufiyaa - MVR Rf</option>
                    <option value="MWK MK">Malawian kwacha - MWK MK</option>
                    <option value="MXN $">Mexican peso - MXN $</option>
                    <option value="MYR RM">Malaysian ringgit - MYR RM</option>
                    <option value="MZN MT">Mozambican metical - MZN MT</option>
                    <option value="NAD $">Namibian dollar - NAD $</option>
                    <option value="NGN ₦">Nigerian naira - NGN ₦</option>
                    <option value="NIO C$">Nicaraguan córdoba - NIO C$</option>
                    <option value="NOK kr">Norwegian krone - NOK kr</option>
                    <option value="NPR Rs">Nepalese rupee - NPR Rs</option>
                    <option value="NZD $">New Zealand dollar - NZD $</option>
                    <option value="OMR ر.ع.">Omani rial - OMR ر.ع.</option>
                    <option value="PAB B/.">Panamanian balboa - PAB B/.</option>
                    <option value="PEN S/.">Peruvian Sol - PEN S/.</option>
                    <option value="PGK K">
                      Papua New Guinean kina - PGK K
                    </option>
                    <option value="PHP ₱">Philippine peso - PHP ₱</option>
                    <option value="PKR Rs">Pakistani rupee - PKR Rs</option>
                    <option value="PLN zł">Polish złoty - PLN zł</option>
                    <option value="PRB ￦">Transnistrian ruble - PRB ￦</option>
                    <option value="PYG ₲">Paraguayan guaraní - PYG ₲</option>
                    <option value="QAR QR">Qatari riyal - QAR QR</option>
                    <option value="RON RON">Romanian leu - RON RON</option>
                    <option value="RSD дин.">Serbian dinar - RSD дин.</option>
                    <option value="RUB руб.">Russian ruble - RUB руб.</option>
                    <option value="RWF RF">Rwandan franc - RWF RF</option>
                    <option value="SAR ر.س">Saudi riyal - SAR ر.س</option>
                    <option value="SBD $">
                      Solomon Islands dollar - SBD $
                    </option>
                    <option value="SCR Rs">Seychellois rupee - SCR Rs</option>
                    <option value="SDG ج.س">Sudanese pound - SDG ج.س</option>
                    <option value="SEK kr">
                      Swedish krona/kronor - SEK kr
                    </option>
                    <option value="SGD $">Singapore dollar - SGD $</option>
                    <option value="SHP £">Saint Helena pound - SHP £</option>
                    <option value="SLL Le">
                      Sierra Leonean leone - SLL Le
                    </option>
                    <option value="SOS Sh">Somali shilling - SOS Sh</option>
                    <option value="SRD $">Surinamese dollar - SRD $</option>
                    <option value="SSP £">South Sudanese pound - SSP £</option>
                    <option value="SVC $">Salvadoran colón - SVC $</option>
                    <option value="SYP £">Syrian pound - SYP £</option>
                    <option value="SZL L">Swazi lilangeni - SZL L</option>
                    <option value="THB ฿">Thai baht - THB ฿</option>
                    <option value="TJS ЅМ">Tajikistani somoni - TJS ЅМ</option>
                    <option value="TMT m">Turkmenistan manat - TMT m</option>
                    <option value="TND د.ت">Tunisian dinar - TND د.ت</option>
                    <option value="TOP T$">Tongan paʻanga - TOP T$</option>
                    <option value="TRY TL">Turkish lira - TRY TL</option>
                    <option value="TWD $">New Taiwan dollar - TWD $</option>
                    <option value="TZS Sh">Tanzanian shilling - TZS Sh</option>
                    <option value="UAH ₴">Ukrainian hryvnia - UAH ₴</option>
                    <option value="UGX Sh">Ugandan shilling - UGX Sh</option>
                    <option value="UYU $">Uruguayan peso - UYU $</option>
                    <option value="UZS лв">Uzbekistan som - UZS лв</option>
                    <option value="VES Bs">Venezuelan bolívar - VES Bs</option>
                    <option value="VND ₫">Vietnamese đồng - VND ₫</option>
                    <option value="VUV VT">Vanuatu vatu - VUV VT</option>
                    <option value="WST T">Samoan tala - WST T</option>
                    <option value="XAG $">
                      Silver (one troy ounce) - XAG $
                    </option>
                    <option value="XAU $">Gold (one troy ounce) - XAU $</option>
                    <option value="XCD $">East Caribbean dollar - XCD $</option>
                    <option value="XDR £">
                      Special drawing rights - XDR £
                    </option>
                    <option value="XPF FCFP">CFP franc - XPF FCFP</option>
                    <option value="XSU $">Sucre - XSU $</option>
                    <option value="XUA $">ADB Unit of Account - XUA $</option>
                    <option value="XXX $">No currency - XXX $</option>
                    <option value="YER ﷼">Yemeni rial - YER ﷼</option>
                    <option value="ZAR R">South African rand - ZAR R</option>
                    <option value="ZMW Kw">Zambian kwacha - ZMW Kw</option>
                    <option value="ZWL $">Zimbabwean dollar - ZWL $</option>
                  </select>
                </div>
              </div>

              <div>
                <h2
                  id="payment-details-heading"
                  class="text-lg font-medium leading-6"
                >
                  <Icon
                    name="ph:map-pin-duotone"
                    class="inline h-9 w-9 mr-2 text-primary-500 p-2 border border-primary-800/30 bg-primary-600/10 rounded-full"
                  />
                  Shop Address
                </h2>
                <p class="mt-1 text-sm text-gray-500 pl-12 dark:text-slate-300">
                  Please note that updating your location could take few minutes
                  to take effect.
                </p>
              </div>

              <div class="mt-6 grid grid-cols-4 gap-6">
                <div class="col-span-4 sm:col-span-2">
                  <label for="email-address" class="block text-sm font-medium"
                    >Email</label
                  >
                  <input
                    v-model="shop.email"
                    type="text"
                    name="email-address"
                    id="email-address"
                    autocomplete="email"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>
                <div class="col-span-4 sm:col-span-2">
                  <label for="email-address" class="block text-sm font-medium"
                    >Phone</label
                  >
                  <input
                    v-model="shop.phone"
                    type="text"
                    name="email-address"
                    id="email-address"
                    autocomplete="email"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>

                <div class="col-span-4 sm:col-span-2">
                  <label for="email-address" class="block text-sm font-medium"
                    >Street Address</label
                  >
                  <input
                    v-model="shop.street"
                    type="text"
                    name="email-address"
                    id="email-address"
                    autocomplete="email"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>

                <div class="col-span-4 sm:col-span-1">
                  <label for="city" class="block text-sm font-medium"
                    >City</label
                  >
                  <input
                    v-model="shop.city"
                    type="text"
                    name="city"
                    id="city"
                    autocomplete="cc-csc"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>

                <div class="col-span-4 sm:col-span-1">
                  <label
                    for="security-code"
                    class="flex items-center text-sm font-medium"
                  >
                    <span>State</span>
                    <QuestionMarkCircleIcon
                      class="ml-1 h-5 w-5 flex-shrink-0 text-gray-300"
                      aria-hidden="true"
                    />
                  </label>
                  <input
                    v-model="shop.state"
                    type="text"
                    name="security-code"
                    id="security-code"
                    autocomplete="cc-csc"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>

                <div class="col-span-4 sm:col-span-2">
                  <label for="country" class="block text-sm font-medium"
                    >Country</label
                  >
                  <select
                    v-model="shop.country"
                    id="country"
                    name="country"
                    autocomplete="country-name"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  >
                    <option value="">Select Country</option>
                    <option
                      v-for="con in countries"
                      :value="con.code2"
                      :key="con.name"
                    >
                      {{ con.name }}
                    </option>
                  </select>
                </div>

                <div class="col-span-4 sm:col-span-2">
                  <label for="postal-code" class="block text-sm font-medium"
                    >ZIP / Postal code</label
                  >
                  <input
                    v-model="shop.zip_code"
                    type="text"
                    name="postal-code"
                    id="postal-code"
                    autocomplete="postal-code"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>
              </div>

              <div shape="rounded" class="mt-10">
                <h2
                  id="payment-details-heading"
                  class="text-lg font-medium leading-6"
                >
                  <Icon
                    name="ph:device-mobile-camera-duotone"
                    class="inline h-9 w-9 mr-2 text-primary-500 p-2 border border-primary-800/30 bg-primary-600/10 rounded-full"
                  />
                  Mobile App Links
                </h2>
                <p class="mt-1 text-sm text-gray-500 pl-12 dark:text-slate-300">
                  Leave it blank if you don't hove apps.
                </p>
              </div>
              <div class="mt-4 mb-10 grid grid-cols-4 gap-6">
                <div class="col-span-4 sm:col-span-2">
                  <label for="email-address" class="block text-sm font-medium">
                    <Icon
                      name="material-symbols-light:ios"
                      class="inline h-5 w-5 mr-2"
                    />
                    Android App Link</label
                  >
                  <input
                    v-model="shop.android_app_link"
                    type="text"
                    name="email-address"
                    id="email-address"
                    autocomplete="email"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>
                <div class="col-span-4 sm:col-span-2">
                  <label for="email-address" class="block text-sm font-medium">
                    <Icon
                      name="material-symbols:android"
                      class="inline h-5 w-5 mr-2"
                    />
                    IOS App Link</label
                  >
                  <input
                    v-model="shop.ios_app_link"
                    type="text"
                    name="email-address"
                    id="email-address"
                    autocomplete="email"
                    class="mt-1 block w-full rounded-md border border-gray-300 py-2 px-3 -sm focus:border-gray-900 focus:outline-none focus:ring-gray-900 sm:text-sm"
                  />
                </div>
              </div>
              <div class="mt-8" v-if="shop.local_active">
                <h2
                  id="payment-details-heading"
                  class="text-lg font-medium leading-6"
                >
                  <Icon
                    name="ph:storefront-duotone"
                    class="inline h-9 w-9 mr-2 text-primary-500 p-2 border border-primary-800/30 bg-primary-600/10 rounded-full"
                  />
                  Local Storage Settings
                </h2>
                <p class="mt-1 text-sm text-gray-500 pl-12">
                  Please note that updating your location could take few minutes
                  to take effect.
                </p>
              </div>

              <div class="mt-4 flex flex-wrap gap-6" v-if="shop.local_active">
                <div class="flex gap-2">
                  <input
                    type="checkbox"
                    name="warehouse1"
                    id="warehouse1"
                    v-model="shop.warehouse"
                    class="cursor-pointer"
                  />
                  <label
                    for="warehouse1"
                    class="cursor-pointer block text-sm font-medium"
                    >Warehouse</label
                  >
                </div>
                <div class="flex gap-2">
                  <input
                    type="checkbox"
                    name="room1"
                    id="room1"
                    v-model="shop.room"
                    class="cursor-pointer"
                  />
                  <label
                    for="room1"
                    class="cursor-pointer block text-sm font-medium"
                    >Room</label
                  >
                </div>
                <div class="flex gap-2">
                  <input
                    type="checkbox"
                    name="sec1"
                    id="sec1"
                    v-model="shop.sec"
                    class="cursor-pointer"
                  />
                  <label
                    for="sec1"
                    class="cursor-pointer block text-sm font-medium"
                    >Section</label
                  >
                </div>
                <div class="flex gap-2">
                  <input
                    type="checkbox"
                    name="shelf1"
                    id="shelf1"
                    v-model="shop.shelf"
                    class="cursor-pointer"
                  />
                  <label
                    for="shelf1"
                    class="cursor-pointer block text-sm font-medium"
                    >Shelf</label
                  >
                </div>
                <div class="flex gap-2">
                  <input
                    type="checkbox"
                    name="rack1"
                    id="rack1"
                    v-model="shop.rack"
                    class="cursor-pointer"
                  />
                  <label
                    for="rack1"
                    class="cursor-pointer block text-sm font-medium"
                    >Rack</label
                  >
                </div>
                <div class="flex gap-2">
                  <input
                    type="checkbox"
                    name="drawer1"
                    id="drawer1"
                    v-model="shop.drawer"
                    class="cursor-pointer"
                  />
                  <label
                    for="drawer1"
                    class="cursor-pointer block text-sm font-medium"
                    >Drawer</label
                  >
                </div>
                <div class="flex gap-2">
                  <input
                    type="checkbox"
                    name="file1"
                    id="file1"
                    v-model="shop.file"
                    class="cursor-pointer"
                  />
                  <label
                    for="file1"
                    class="cursor-pointer block text-sm font-medium"
                    >File</label
                  >
                </div>
              </div>
            </div>
            <BaseCard class="px-4 py-3 text-right sm:px-6">
              <BaseButton
                color="primary"
                v-if="!loading"
                @click="updateShop"
                type="submit"
                class="inline-flex justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
              >
                Save
              </BaseButton>
              <button
                v-else
                class="inline-flex justify-center rounded-md border border-transparent bg-gray-800 py-2 px-4 text-sm font-medium text-white -sm hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="22"
                  height="22"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
                    opacity=".25"
                  />
                  <path
                    fill="currentColor"
                    d="M10.14,1.16a11,11,0,0,0-9,8.92A1.59,1.59,0,0,0,2.46,12,1.52,1.52,0,0,0,4.11,10.7a8,8,0,0,1,6.66-6.61A1.42,1.42,0,0,0,12,2.69h0A1.57,1.57,0,0,0,10.14,1.16Z"
                  >
                    <animateTransform
                      attributeName="transform"
                      dur="0.75s"
                      repeatCount="indefinite"
                      type="rotate"
                      values="0 12 12;360 12 12"
                    />
                  </path>
                </svg>
              </button>
            </BaseCard>
          </div>
        </BaseCard>
      </section>
    </div>
  </div>
</template>

<script setup>
import { QuestionMarkCircleIcon } from "@heroicons/vue/24/outline";
const { shop, getShop } = useShop();
const Api = useApi();
const { notifs } = useAuth();
const loading = ref(false);
async function updateShop() {
  loading.value = true;
  const res = await Api.post("/api/ecommerce/dash/shop", shop.value);
  console.log("res", res.data);
  loading.value = false;
  notifs.value.push({
    type: "success",
    message: "Shop updated successfully",
  });
  await getShop();
}
function logoUploaded(e) {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.onload = (e) => {
    shop.value.newLogo = e.target.result;
  };
  reader.readAsDataURL(file);
}
function favUploaded(e) {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.onload = (e) => {
    shop.value.newFavicon = e.target.result;
  };
  reader.readAsDataURL(file);
}
function paymentLogosUploaded(e) {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.onload = (e) => {
    shop.value.newPayment_image = e.target.result;
  };
  reader.readAsDataURL(file);
}

const countries = ref([]);
function getCountries() {
  Api.get("/api/utils/countries/").then((res) => {
    countries.value = res.data;
  });
}
getCountries();
</script>

<style scoped></style>
