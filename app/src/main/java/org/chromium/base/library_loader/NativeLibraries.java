package org.chromium.base.library_loader;
import org.chromium.base.annotations.SuppressFBWarnings;
@SuppressFBWarnings
public class NativeLibraries {
    public static boolean sUseLinker = false;
    public static boolean sUseLibraryInZipFile = false;
    public static boolean sEnableLinkerTests = false;
    public static final String[] LIBRARIES =
      {"c++_shared","mojo_public_system.cr","base.cr","gin_features.cr","ffmpeg.cr","device_event_log.cr","discardable_memory_common.cr","gles2_c_lib.cr","display_types.cr","sandbox_services.cr","platform.cr","prefs.cr","mojo_public_system_cpp.cr","startup_tracing.cr","v8_libbase.cr","range.cr","gles2_utils.cr","geometry.cr","protobuf_lite.cr","user_prefs.cr","seccomp_bpf.cr","common.cr","icuuc.cr","device_base.cr","mojo_common_lib.cr","keyed_service_core.cr","bindings.cr","boringssl.cr","service_manager_mojom_shared.cr","url.cr","device_gamepad.cr","url_ipc.cr","blink_mojo_bindings_shared.cr","crcrypto.cr","freetype.cr","policy_proto.cr","ui_data_pack.cr","resource_coordinator_public_interfaces_internal_shared.cr","generic_sensor_public_interfaces_shared.cr","icui18n.cr","blink_android_mojo_bindings_shared.cr","sensors.cr","public.cr","discardable_memory_client.cr","chromium_sqlite3.cr","cloud_policy_proto_generated_compile.cr","v8.cr","fingerprint.cr","device_vr_mojo_bindings_shared.cr","onc.cr","wtf.cr","display_util.cr","events_base.cr","sql.cr","shared_memory_support.cr","keyed_service_content.cr","discardable_memory_service.cr","content_common_mojo_bindings_shared.cr","ipc_mojom_shared.cr","service_manager_mojom_constants_shared.cr","url_matcher.cr","skia.cr","mojo_system_impl.cr","service_manager_mojom_blink.cr","gin.cr","blink_offscreen_canvas_mojo_bindings_shared.cr","webdata_common.cr","base_i18n.cr","cpp.cr","service_manager_mojom_constants.cr","service_manager_cpp_types.cr","color_space.cr","display.cr","geometry_skia.cr","service_manager_mojom_constants_blink.cr","ipc_mojom.cr","surface.cr","codec.cr","animation.cr","net.cr","js.cr","generic_sensor.cr","cc_debug.cr","midi.cr","geolocation.cr","service_manager_mojom.cr","proxy_config.cr","devices.cr","ipc.cr","net_with_v8.cr","cc_base.cr","storage_common.cr","captive_portal.cr","gfx_ipc_geometry.cr","gfx_ipc_skia.cr","service_manager_cpp.cr","tracing.cr","gfx_ipc_color.cr","storage_browser.cr","cc_paint.cr","gfx.cr","user_manager.cr","resource_coordinator_cpp.cr","gfx_ipc.cr","ui_touch_selection.cr","message_center.cr","gesture_detection.cr","printing.cr","gl_wrapper.cr","events.cr","ui_base.cr","bluetooth.cr","native_theme.cr","policy_component.cr","accessibility.cr","ui_base_ime.cr","embedder.cr","manager.cr","gl_init.cr","gpu.cr","gles2_implementation.cr","gl_in_process_context.cr","media.cr","device_vr_mojo_bindings_blink.cr","device_vr_mojo_bindings.cr","cdm_manager.cr","capture_base.cr","capture_lib.cr","media_gpu.cr","device_vr.cr","cc.cr","display_compositor.cr","cc_ipc.cr","media_mojo_services.cr","cc_surfaces.cr","cc_animation.cr","snapshot.cr","ui_android.cr","shell_dialogs.cr","blink_platform.cr","frame_sinks.cr","blink_core.cr","compositor.cr","power_save_blocker.cr","blink_modules.cr","cc_blink.cr","blink_web.cr","media_blink.cr","content.cr","domain_reliability.cr","web_dialogs.cr","sessions.cr","chrome.cr"};
    static String sVersionNumber =
      "60.0.3112.20";
}
