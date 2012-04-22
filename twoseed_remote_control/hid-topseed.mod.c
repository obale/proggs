#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
 .name = KBUILD_MODNAME,
 .init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
 .exit = cleanup_module,
#endif
 .arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x3f0d134b, "module_layout" },
	{ 0x5b45f49e, "__hid_register_driver" },
	{ 0xea147363, "printk" },
	{ 0x65125d5, "hid_unregister_driver" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=hid";

MODULE_ALIAS("hid:b0003v00000766p00000204");
