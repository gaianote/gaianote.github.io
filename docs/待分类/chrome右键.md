create -help

integer Chrome.contextMenus.create(object createProperties, function callback)
创建一个新的右键菜单项。注意：如果在创建的过程中出现错误，会在回调函数触发后才能捕获到，错误详细信息保存在Chrome.extension.lastError中。

【参数】
createProperties ( object )
	type ( optional enumerated string ["normal", "checkbox", "radio", "separator"] )
		右键菜单项的类型。默认为“normal”。
	title ( optional string )
		右键菜单项的显示文字；除非为“separator”类型，否则此参数是必须的。如果类型为“selection”，您可以在字符串中使用%s显示选定的文本。例如，如果参数的值为 "Translate '%s' to Pig Latin"，而用户还选中了文本“cool”，那么显示在菜单中的将会是 "Translate 'cool' to Pig Latin"。
	checked ( optional boolean )
		Checkbox或者radio的初始状态：true代表选中，false代表未选中。在给定的radio中只能有一个处于选中状态。
	contexts ( optional array of string ["all", "page", "frame", "selection", "link", "editable", "image", "video", "audio"] )
		右键菜单项将会在这个列表指定的上下文类型中显示。默认为“page”。
	onclick ( optional function )
		当菜单项被点击时触发的函数。
		【参数】
		info ( OnClickData )
			右键菜单项被点击时相关的上下文信息。
		tab ( Tab )
			右键菜单项被点击时，当前标签的详细信息。
	parentId ( optional integer )
		右键菜单项的父菜单项ID。指定父菜单项将会使此菜单项成为父菜单项的子菜单。
	documentUrlPatterns ( optional array of string )
		这使得右键菜单只在匹配此模式的url页面上生效（这个对框架也适用）。详细的匹配格式见：模式匹配页面。
	targetUrlPatterns ( optional array of string )
		类似于documentUrlPatterns，但是您可以针对img/audio/video标签的src属性和anchor标签的href做过滤。
	enabled ( optional boolean )
		启用或者禁用此菜单项，启用为true，禁用为false。默认为true。
callback ( optional function )
	在创建完菜单项后触发。如果创建过程中有错误产生，其详细信息在Chrome.extension.lastError中。