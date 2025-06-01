<template>
    <div class="border my-8">
        <p class="text-center py-5 w-full text-lg">Barcode Value: {{ barcodeValue }}</p>
        <div class="flex gap-1 w-full justify-center p-4 pb-12">
            <input type="number" class="px-2 bg-slate-200" v-model="qty">
            <button class="bg-blue-600 px-2 py-2 rounded-sm text-white" type="button" @click="generateNow();" id="generate-now">GENERATE</button>
            <button class="bg-blue-600 px-2 py-2 rounded-sm text-white" v-if="generated" @click="printDiv()">PRINT</button>
        </div>
        <div style="display:flex;gap: 8px;flex-wrap: wrap; justify-content: center;" class="py-10" id="pdfSection">
            <img v-for="index in qty" :key="index" :id="'barcode-' + index">
        </div>
    </div>
</template>

<script setup>
    useHead({
        script: [
            { src: 'https://cdnjs.cloudflare.com/ajax/libs/jsbarcode/3.11.5/JsBarcode.all.min.js', body: true, defer: false },
        ]
    })
    definePageMeta({
        layout: 'ecommerce'
    })
    const route = useRoute()
    const barcodeValue = route.params.id
    const qty = ref(50)
    const barcodeHeight = 40
    const generated = ref(false)

    function generateNow() {
        if(qty < 1) return
        for (let i = 1; i <= qty.value; i++) {
            JsBarcode("#barcode-" + i, barcodeValue, {
                height: barcodeHeight,
                fontSize: 17
            });
        }
        generated.value = true
    }
    function printDiv() {
        var divContents = document.getElementById("pdfSection").innerHTML;
        var a = window.open('', '', 'height=auto, width=auto');
        a.document.write('<html><title>Product ID:'+ barcodeValue +'</title> <body >');
        a.document.write(divContents);
        a.document.write('</body></html>');
        a.document.close();
        a.print();
    }
</script>

<style scoped>
</style>
