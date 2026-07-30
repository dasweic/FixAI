import 'package:flex_color_scheme/flex_color_scheme.dart';
import 'package:flutter/material.dart';

class AppTheme {
  static ThemeData get light => FlexThemeData.light(useMaterial3: true);

  static ThemeData get dark => FlexThemeData.dark(useMaterial3: true);
}