<template>
	<section class="editor">
		<span ref="editorButtons"></span>
		<div
			class="head flex flex-wrap gap-[3px]"
			:class="{ stickyButtons: editorButtonsTop < 30 }"
		>
			<button class="!p-0 relative">
				<input
					class="w-full h-full opacity-0"
					type="color"
					@input="
						editor
							.chain()
							.focus()
							.setHighlight({ color: $event.target.value })
							.run()
					"
					:value="editor.getAttributes('highlight').color || '#000000'"
				/>
				<UIcon
					name="i-material-symbols-format-color-fill"
					:style="'color:' + editor.getAttributes('highlight').color"
					dynamic
					class="absolute pointer-events-none"
				/>
			</button>
			<button class="!p-0 relative cursor-pointer">
				<input
					class="w-full h-full opacity-0 cursor-pointer"
					type="color"
					@input="editor.chain().focus().setColor($event.target.value).run()"
					:value="editor.getAttributes('textStyle').color || '#000000'"
				/>
				<UIcon
					name="i-material-symbols-format-color-text"
					:style="'color:' + editor.getAttributes('textStyle').color"
					dynamic
					class="absolute pointer-events-none"
				/>
			</button>
			<button
				@click="editor.chain().focus().toggleBold().run()"
				:disabled="!editor.can().chain().focus().toggleBold().run()"
				:class="{ 'is-active': editor.isActive('bold') }"
			>
				B
			</button>
			<button
				@click="editor.chain().focus().toggleItalic().run()"
				:disabled="!editor.can().chain().focus().toggleItalic().run()"
				:class="{ 'is-active': editor.isActive('italic') }"
			>
				<UIcon
					name="i-ph-text-italic"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				@click="editor.chain().focus().toggleStrike().run()"
				:disabled="!editor.can().chain().focus().toggleStrike().run()"
				:class="{ 'is-active': editor.isActive('strike') }"
			>
				<del>S</del>
			</button>
			<button @click="editor.chain().focus().unsetAllMarks().run()">
				<UIcon
					name="i-mingcute-broom-line"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				@click="editor.chain().focus().setParagraph().run()"
				:class="{ 'is-active': editor.isActive('paragraph') }"
			>
				P
			</button>
			<button
				@click="editor.chain().focus().toggleHeading({ level: 1 }).run()"
				:class="{ 'is-active': editor.isActive('heading', { level: 1 }) }"
			>
				H1
			</button>
			<button
				@click="editor.chain().focus().toggleHeading({ level: 2 }).run()"
				:class="{ 'is-active': editor.isActive('heading', { level: 2 }) }"
			>
				H2
			</button>
			<button
				@click="editor.chain().focus().toggleHeading({ level: 3 }).run()"
				:class="{ 'is-active': editor.isActive('heading', { level: 3 }) }"
			>
				H3
			</button>
			<button
				@click="editor.chain().focus().toggleHeading({ level: 4 }).run()"
				:class="{ 'is-active': editor.isActive('heading', { level: 4 }) }"
			>
				H4
			</button>
			<button
				@click="editor.chain().focus().toggleHeading({ level: 5 }).run()"
				:class="{ 'is-active': editor.isActive('heading', { level: 5 }) }"
			>
				H5
			</button>
			<button
				@click="editor.chain().focus().toggleHeading({ level: 6 }).run()"
				:class="{ 'is-active': editor.isActive('heading', { level: 6 }) }"
			>
				H6
			</button>
			<button
				@click="editor.chain().focus().toggleBulletList().run()"
				:class="{ 'is-active': editor.isActive('bulletList') }"
			>
				<UIcon
					name="i-ic-format-list-bulleted"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				@click="editor.chain().focus().toggleOrderedList().run()"
				:class="{ 'is-active': editor.isActive('orderedList') }"
			>
				<UIcon
					name="i-ic-format-list-numbered"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				@click="editor.chain().focus().toggleCode().run()"
				:disabled="!editor.can().chain().focus().toggleCode().run()"
				:class="{ 'is-active': editor.isActive('code') }"
			>
				<UIcon
					name="i-ic-outline-code"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				@click="editor.chain().focus().toggleCodeBlock().run()"
				:class="{ 'is-active': editor.isActive('codeBlock') }"
			>
				<UIcon
					name="i-material-symbols-light-terminal"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				@click="editor.chain().focus().toggleBlockquote().run()"
				:class="{ 'is-active': editor.isActive('blockquote') }"
			>
				<UIcon
					name="i-ic-format-quote"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button @click="editor.chain().focus().clearNodes().run()">
				<UIcon
					name="i-mingcute-broom-line"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button @click="editor.chain().focus().setHorizontalRule().run()">
				<UIcon
					name="i-ic-sharp-horizontal-rule"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button @click="editor.chain().focus().setHardBreak().run()">
				<UIcon
					name="i-codicon-newline"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				class="relative z-20"
				@click="imageSelector = true"
				:class="{ 'is-active': tableSlide }"
			>
				<UIcon
					name="i-heroicons-photo"
					dynamic
				/>
				<USlideover v-model="imageSelector">
					<div class="flex items-center justify-between w-full px-4 py-2">
						<h3
							class="text-base font-semibold leading-6 text-gray-900 dark:text-white flex-1"
						>
							Browse Images
						</h3>

						<UIcon
							@click="imageSelector = false"
							name="i-heroicons-x-mark-20-solid"
							class="w-7 h-7 cursor-pointer"
						/>
					</div>
					<CommonImageBrowser
						:url="'/api/blog/post-images/?pid=' + pid"
						class="px-4"
						@selected="imageSelected"
					/>
				</USlideover>
			</button>
			<button
				class="relative z-20"
				@click="tableSlide = !tableSlide"
				:class="{ 'is-active': tableSlide }"
			>
				<UIcon
					name="i-mdi-table"
					dynamic
				/>
				<USlideover
					class="table-slide-over"
					v-model="tableSlide"
				>
					<div class="flex items-center justify-between w-full px-4 py-2">
						<h3
							class="text-base font-semibold leading-6 text-gray-900 dark:text-white flex-1"
						>
							Table
						</h3>

						<UIcon
							@click="tableSlide = false"
							name="i-heroicons-x-mark-20-solid"
							class="w-7 h-7 cursor-pointer"
						/>
					</div>
					<div class="overflow-y-scroll p-2">
						<button
							@click="
								editor
									.chain()
									.focus()
									.insertTable({ rows: 3, cols: 3, withHeaderRow: true })
									.run()
							"
						>
							Insert Table
						</button>
						<button
							@click="editor.chain().focus().addColumnBefore().run()"
							:disabled="!editor.can().addColumnBefore()"
						>
							Add Column Before
						</button>
						<button
							@click="editor.chain().focus().addColumnAfter().run()"
							:disabled="!editor.can().addColumnAfter()"
						>
							Add Column After
						</button>
						<button
							@click="editor.chain().focus().deleteColumn().run()"
							:disabled="!editor.can().deleteColumn()"
						>
							Delete Column
						</button>
						<button
							@click="editor.chain().focus().addRowBefore().run()"
							:disabled="!editor.can().addRowBefore()"
						>
							Add Row Before
						</button>
						<button
							@click="editor.chain().focus().addRowAfter().run()"
							:disabled="!editor.can().addRowAfter()"
						>
							Add Row After
						</button>
						<button
							@click="editor.chain().focus().deleteRow().run()"
							:disabled="!editor.can().deleteRow()"
						>
							Delete Row
						</button>
						<button
							@click="editor.chain().focus().deleteTable().run()"
							:disabled="!editor.can().deleteTable()"
						>
							Delete Table
						</button>
						<button
							@click="editor.chain().focus().mergeCells().run()"
							:disabled="!editor.can().mergeCells()"
						>
							Merge Cells
						</button>
						<button
							@click="editor.chain().focus().splitCell().run()"
							:disabled="!editor.can().splitCell()"
						>
							Split Cell
						</button>
						<button
							@click="editor.chain().focus().toggleHeaderColumn().run()"
							:disabled="!editor.can().toggleHeaderColumn()"
						>
							Toggle Header Column
						</button>
						<button
							@click="editor.chain().focus().toggleHeaderRow().run()"
							:disabled="!editor.can().toggleHeaderRow()"
						>
							Toggle Header Row
						</button>
						<button
							@click="editor.chain().focus().toggleHeaderCell().run()"
							:disabled="!editor.can().toggleHeaderCell()"
						>
							Toggle Header Cell
						</button>
						<button
							@click="editor.chain().focus().mergeOrSplit().run()"
							:disabled="!editor.can().mergeOrSplit()"
						>
							Merge Or Split
						</button>
						<button
							@click="
								editor
									.chain()
									.focus()
									.setCellAttribute('backgroundColor', '#FAF594')
									.run()
							"
							:disabled="
								!editor.can().setCellAttribute('backgroundColor', '#FAF594')
							"
						>
							Set Cell Attribute
						</button>
						<button
							@click="editor.chain().focus().fixTables().run()"
							:disabled="!editor.can().fixTables()"
						>
							Fix Tables
						</button>
						<button
							@click="editor.chain().focus().goToNextCell().run()"
							:disabled="!editor.can().goToNextCell()"
						>
							Go To Next Cell
						</button>
						<button
							@click="editor.chain().focus().goToPreviousCell().run()"
							:disabled="!editor.can().goToPreviousCell()"
						>
							Go To Previous Cell
						</button>
					</div>
				</USlideover>
			</button>
			<button
				@click="editor.chain().focus().undo().run()"
				:disabled="!editor.can().chain().focus().undo().run()"
			>
				<UIcon
					name="i-material-symbols-undo"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
			<button
				@click="editor.chain().focus().redo().run()"
				:disabled="!editor.can().chain().focus().redo().run()"
			>
				<UIcon
					name="i-material-symbols-redo"
					class="w-4 h-4 md:w-6 md:h-6"
					dynamic
				/>
			</button>
		</div>
		<div
			ref="editorButtons"
			class="prose dark:prose-invert prose-sm sm:prose-base lg:prose-lg focus:outline-none min-w-full bg-[#eeeeeed6] dark:bg-[#202a38] rounded-lg"
		>
			<editor-content
				class="p-2"
				:editor="editor"
			/>
		</div>
	</section>
</template>

<script setup>
	import { useElementBounding } from "@vueuse/core";
	import { Editor, EditorContent } from "@tiptap/vue-3";
	import StarterKit from "@tiptap/starter-kit";
	import TextStyle from "@tiptap/extension-text-style";
	import { Color } from "@tiptap/extension-color";
	import Image from "@tiptap/extension-image";
	import Table from "@tiptap/extension-table";
	import TableCell from "@tiptap/extension-table-cell";
	import TableHeader from "@tiptap/extension-table-header";
	import TableRow from "@tiptap/extension-table-row";
	import Highlight from "@tiptap/extension-highlight";

	const imageSelector = ref(false);
	const tableSlide = ref(false);

	const props = defineProps({
		content: String,
		pid: Number | String,
	});
	const emit = defineEmits(["updateContent"]);

	const editor = new Editor({
		extensions: [
			StarterKit,
			TextStyle,
			Color,
			Highlight.configure({
				multicolor: true,
			}),
			Table.configure({
				resizable: false,
			}),
			TableRow,
			TableHeader,
			TableCell,
			Image.configure({
				inline: true,
				HTMLAttributes: {
					class: "my-custom-class",
				},
			}),
		],
		content: "",
		onUpdate: () => {
			emit("updateContent", editor.getHTML());
		},
	});

	onBeforeUnmount(() => {
		editor.destroy();
	});

	const editorButtons = ref(null);
	const { top: editorButtonsTop } = useElementBounding(editorButtons);

	function imageSelected(url) {
		imageSelector.value = false;
		var base = "https://media.devuly.com/f_webp&q_90";
		// var base = "http://127.0.0.1:8000";
		console.log(url);
		editor.commands.setImage({
			src: base + url,
			alt: "A boring example image",
			title: "An example",
		});
	}
	onMounted(() => {
		setTimeout(() => {
			editor.commands.insertContent(props.content);
		}, 1500);
	});
</script>

<style>
	.editor .head button,
	.table-slide-over button {
		padding: 4px 5px;
		border: 1px solid rgba(126, 126, 126, 0.322);
		width: 33px;
		height: 33px;
		font-size: 15px;
		display: flex;
		justify-content: center;
		align-items: center;
		color: rgb(73, 73, 73);
		cursor: pointer;
		border-radius: 10px;
		font-weight: normal;
	}
	.editor .head button:hover,
	.table-slide-over button:hover {
		background: #bbbbbb56;
	}
	.dark .editor .head button,
	.dark .table-slide-over button {
		color: rgb(200, 200, 200);
	}
	.table-slide-over button {
		white-space: nowrap;
		width: 100%;
		text-align: left;
		display: block;
		padding: 2px 20px;
	}
	.editor .head button:disabled,
	.table-slide-over button:disabled {
		opacity: 0.5;
	}
	.editor .head button.is-active,
	.table-slide-over button.is-active {
		background: #bbbbbb56;
	}
	.editor .tiptap {
		outline: none;
		width: 100%;
		height: 70vh;
		min-height: 400px;
		max-height: 800px;
		overflow-y: scroll;
	}
	.prose th,
	.prose td {
		border: 1px solid gray;
		padding: 5px;
		min-width: 120px;
	}
	.prose * {
		margin-top: 5px !important;
		margin-bottom: 5px !important;
	}
	.stickyButtons {
		position: sticky;
		top: 0;
		padding: 5px 0px;
		background-color: #f1f1f1;
		z-index: 5;
	}
	.dark .stickyButtons {
		background-color: #121928;
	}
</style>
