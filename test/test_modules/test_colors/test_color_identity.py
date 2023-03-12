import unittest

from core.colors.color_identity import ColorIdentity


class TestColorIdentity(unittest.TestCase):
    # region Orderings
    wubrg_order = [
        ColorIdentity.C,
        ColorIdentity.W, ColorIdentity.U, ColorIdentity.B, ColorIdentity.R, ColorIdentity.G,
        ColorIdentity.WU, ColorIdentity.WB, ColorIdentity.WR, ColorIdentity.WG, ColorIdentity.UB,
        ColorIdentity.UR, ColorIdentity.UG, ColorIdentity.BR, ColorIdentity.BG, ColorIdentity.RG,
        ColorIdentity.WUB, ColorIdentity.WUR, ColorIdentity.WUG, ColorIdentity.WBR, ColorIdentity.WBG,
        ColorIdentity.WRG, ColorIdentity.UBR, ColorIdentity.UBG, ColorIdentity.URG, ColorIdentity.BRG,
        ColorIdentity.WUBR, ColorIdentity.WUBG, ColorIdentity.WURG, ColorIdentity.WBRG, ColorIdentity.UBRG,
        ColorIdentity.WUBRG,
    ]

    pentad_order = [
        ColorIdentity.C,
        ColorIdentity.W, ColorIdentity.U, ColorIdentity.B, ColorIdentity.R, ColorIdentity.G,
        ColorIdentity.WU, ColorIdentity.UB, ColorIdentity.BR, ColorIdentity.RG, ColorIdentity.WG,
        ColorIdentity.WB, ColorIdentity.BG, ColorIdentity.UG, ColorIdentity.UR, ColorIdentity.WR,
        ColorIdentity.WUR, ColorIdentity.UBG, ColorIdentity.WBR, ColorIdentity.URG, ColorIdentity.WBG,
        ColorIdentity.WUB, ColorIdentity.UBR, ColorIdentity.BRG, ColorIdentity.WRG, ColorIdentity.WUG,
        ColorIdentity.WUBR, ColorIdentity.WUBG, ColorIdentity.WURG, ColorIdentity.WBRG, ColorIdentity.UBRG,
        ColorIdentity.WUBRG,
    ]

    deck_order = [
        ColorIdentity.W, ColorIdentity.U, ColorIdentity.B, ColorIdentity.R, ColorIdentity.G,
        ColorIdentity.WU, ColorIdentity.WB, ColorIdentity.WR, ColorIdentity.WG, ColorIdentity.UB,
        ColorIdentity.UR, ColorIdentity.UG, ColorIdentity.BR, ColorIdentity.BG, ColorIdentity.RG,
        ColorIdentity.WUB, ColorIdentity.WUR, ColorIdentity.WUG, ColorIdentity.WBR, ColorIdentity.WBG,
        ColorIdentity.WRG, ColorIdentity.UBR, ColorIdentity.UBG, ColorIdentity.URG, ColorIdentity.BRG,
        ColorIdentity.WUBR, ColorIdentity.WUBG, ColorIdentity.WURG, ColorIdentity.WBRG, ColorIdentity.UBRG,
        ColorIdentity.WUBRG, ColorIdentity.C,
    ]

    value_order = [
        ColorIdentity.C, ColorIdentity.W, ColorIdentity.U, ColorIdentity.WU, ColorIdentity.B, ColorIdentity.WB,
        ColorIdentity.UB, ColorIdentity.WUB, ColorIdentity.R, ColorIdentity.WR, ColorIdentity.UR,
        ColorIdentity.WUR, ColorIdentity.BR, ColorIdentity.WBR, ColorIdentity.UBR, ColorIdentity.WUBR,
        ColorIdentity.G, ColorIdentity.WG, ColorIdentity.UG, ColorIdentity.WUG, ColorIdentity.BG,
        ColorIdentity.WBG, ColorIdentity.UBG, ColorIdentity.WUBG, ColorIdentity.RG, ColorIdentity.WRG,
        ColorIdentity.URG, ColorIdentity.WURG, ColorIdentity.BRG, ColorIdentity.WBRG, ColorIdentity.UBRG,
        ColorIdentity.WUBRG,
    ]
    # endregion Orderings

    def test_color_identity_iter(self):
        # NOTE: This test is _key_. If this fails, the basis of multiple functions is incorrect.
        self.assertEqual(self.wubrg_order, [ci for ci in ColorIdentity])

    def test_inclusion(self):
        self.assertIn(ColorIdentity.C, ColorIdentity.C)
        self.assertIn(ColorIdentity.C, ColorIdentity.U)
        self.assertIn(ColorIdentity.C, ColorIdentity.UR)
        self.assertIn(ColorIdentity.C, ColorIdentity.URG)
        self.assertIn(ColorIdentity.C, ColorIdentity.WURG)
        self.assertIn(ColorIdentity.C, ColorIdentity.WUBRG)
        self.assertNotIn(ColorIdentity.U, ColorIdentity.C)
        self.assertIn(ColorIdentity.U, ColorIdentity.U)
        self.assertIn(ColorIdentity.U, ColorIdentity.UR)
        self.assertIn(ColorIdentity.U, ColorIdentity.URG)
        self.assertIn(ColorIdentity.U, ColorIdentity.WURG)
        self.assertIn(ColorIdentity.U, ColorIdentity.WUBRG)
        self.assertNotIn(ColorIdentity.UR, ColorIdentity.C)
        self.assertNotIn(ColorIdentity.UR, ColorIdentity.U)
        self.assertIn(ColorIdentity.UR, ColorIdentity.UR)
        self.assertIn(ColorIdentity.UR, ColorIdentity.URG)
        self.assertIn(ColorIdentity.UR, ColorIdentity.WURG)
        self.assertIn(ColorIdentity.UR, ColorIdentity.WUBRG)
        self.assertNotIn(ColorIdentity.URG, ColorIdentity.C)
        self.assertNotIn(ColorIdentity.URG, ColorIdentity.U)
        self.assertNotIn(ColorIdentity.URG, ColorIdentity.UR)
        self.assertIn(ColorIdentity.URG, ColorIdentity.URG)
        self.assertIn(ColorIdentity.URG, ColorIdentity.WURG)
        self.assertIn(ColorIdentity.URG, ColorIdentity.WUBRG)
        self.assertNotIn(ColorIdentity.WURG, ColorIdentity.C)
        self.assertNotIn(ColorIdentity.WURG, ColorIdentity.U)
        self.assertNotIn(ColorIdentity.WURG, ColorIdentity.UR)
        self.assertNotIn(ColorIdentity.WURG, ColorIdentity.URG)
        self.assertIn(ColorIdentity.WURG, ColorIdentity.WURG)
        self.assertIn(ColorIdentity.WURG, ColorIdentity.WUBRG)
        self.assertNotIn(ColorIdentity.WUBRG, ColorIdentity.C)
        self.assertNotIn(ColorIdentity.WUBRG, ColorIdentity.U)
        self.assertNotIn(ColorIdentity.WUBRG, ColorIdentity.UR)
        self.assertNotIn(ColorIdentity.WUBRG, ColorIdentity.URG)
        self.assertNotIn(ColorIdentity.WUBRG, ColorIdentity.WURG)
        self.assertIn(ColorIdentity.WUBRG, ColorIdentity.WUBRG)

    def test_aliases(self):
        self.assertListEqual(ColorIdentity.C.aliases, ['C', ''])
        self.assertListEqual(ColorIdentity.W.aliases, ['W', 'White', 'MonoWhite', 'Ardenvale', 'Auriok'])
        self.assertListEqual(ColorIdentity.U.aliases, ['U', 'Blue', 'MonoBlue', 'Vantress', 'Neurok'])
        self.assertListEqual(ColorIdentity.B.aliases, ['B', 'Black', 'MonoBlack', 'Locthwain', 'Moriok'])
        self.assertListEqual(ColorIdentity.R.aliases, ['R', 'Red', 'MonoRed', 'Embereth', 'Vulshok'])
        self.assertListEqual(ColorIdentity.G.aliases, ['G', 'Green', 'MonoGreen', 'Garenbrig', 'Sylvok'])
        self.assertListEqual(ColorIdentity.WU.aliases, ['WU', 'Azorius', 'Ojutai'])
        self.assertListEqual(ColorIdentity.WB.aliases, ['WB', 'Orzhov', 'Silverquill'])
        self.assertListEqual(ColorIdentity.WR.aliases, ['WR', 'Boros', 'Lorehold'])
        self.assertListEqual(ColorIdentity.WG.aliases, ['WG', 'Selesnya', 'Dromoka'])
        self.assertListEqual(ColorIdentity.UB.aliases, ['UB', 'Dimir', 'Silumgar'])
        self.assertListEqual(ColorIdentity.UR.aliases, ['UR', 'Izzet', 'Prismari'])
        self.assertListEqual(ColorIdentity.UG.aliases, ['UG', 'Simic', 'Quandrix'])
        self.assertListEqual(ColorIdentity.BR.aliases, ['BR', 'Rakdos', 'Kolaghan'])
        self.assertListEqual(ColorIdentity.BG.aliases, ['BG', 'Golgari', 'Witherbloom'])
        self.assertListEqual(ColorIdentity.RG.aliases, ['RG', 'Gruul', 'Atarka'])
        self.assertListEqual(ColorIdentity.WUB.aliases, ['WUB', 'Esper', 'Obscura'])
        self.assertListEqual(ColorIdentity.WUR.aliases, ['WUR', 'Jeskai', 'Raugrin', 'Numot', 'Raka'])
        self.assertListEqual(ColorIdentity.WUG.aliases, ['WUG', 'Bant', 'Brokers'])
        self.assertListEqual(ColorIdentity.WBR.aliases, ['WBR', 'Mardu', 'Savai', 'Oros', 'Dega'])
        self.assertListEqual(ColorIdentity.WBG.aliases, ['WBG', 'Abzan', 'Indatha', 'Teneb', 'Necra'])
        self.assertListEqual(ColorIdentity.WRG.aliases, ['WRG', 'Naya', 'Cabaretti'])
        self.assertListEqual(ColorIdentity.UBR.aliases, ['UBR', 'Grixis', 'Maestros'])
        self.assertListEqual(ColorIdentity.UBG.aliases, ['UBG', 'Sultai', 'Zagoth', 'Vorosh', 'Ana'])
        self.assertListEqual(ColorIdentity.URG.aliases, ['URG', 'Temur', 'Ketria', 'Intet', 'Ceta'])
        self.assertListEqual(ColorIdentity.BRG.aliases, ['BRG', 'Jund', 'Riveteers'])
        self.assertListEqual(ColorIdentity.WUBR.aliases, ['WUBR', 'Yore', 'Artifice', 'NonG'])
        self.assertListEqual(ColorIdentity.WUBG.aliases, ['WUBG', 'Witch', 'Growth', 'NonR'])
        self.assertListEqual(ColorIdentity.WURG.aliases, ['WURG', 'Ink', 'Altruism', 'NonB'])
        self.assertListEqual(ColorIdentity.WBRG.aliases, ['WBRG', 'Dune', 'Aggression', 'NonU'])
        self.assertListEqual(ColorIdentity.UBRG.aliases, ['UBRG', 'Glint', 'Chaos', 'NonW'])
        self.assertListEqual(ColorIdentity.WUBRG.aliases, ['WUBRG', 'FiveColor', 'All'])

    def test_by_name(self):
        self.assertEqual(ColorIdentity.C, ColorIdentity.by_name(''))
        self.assertEqual(ColorIdentity.C, ColorIdentity.by_name('C'))
        self.assertEqual(ColorIdentity.W, ColorIdentity.by_name('W'))
        self.assertEqual(ColorIdentity.W, ColorIdentity.by_name('White'))
        self.assertEqual(ColorIdentity.W, ColorIdentity.by_name('MonoWhite'))
        self.assertEqual(ColorIdentity.W, ColorIdentity.by_name('Ardenvale'))
        self.assertEqual(ColorIdentity.W, ColorIdentity.by_name('Auriok'))
        self.assertEqual(ColorIdentity.U, ColorIdentity.by_name('U'))
        self.assertEqual(ColorIdentity.U, ColorIdentity.by_name('Blue'))
        self.assertEqual(ColorIdentity.U, ColorIdentity.by_name('MonoBlue'))
        self.assertEqual(ColorIdentity.U, ColorIdentity.by_name('Vantress'))
        self.assertEqual(ColorIdentity.U, ColorIdentity.by_name('Neurok'))
        self.assertEqual(ColorIdentity.B, ColorIdentity.by_name('B'))
        self.assertEqual(ColorIdentity.B, ColorIdentity.by_name('Black'))
        self.assertEqual(ColorIdentity.B, ColorIdentity.by_name('MonoBlack'))
        self.assertEqual(ColorIdentity.B, ColorIdentity.by_name('Locthwain'))
        self.assertEqual(ColorIdentity.B, ColorIdentity.by_name('Moriok'))
        self.assertEqual(ColorIdentity.R, ColorIdentity.by_name('R'))
        self.assertEqual(ColorIdentity.R, ColorIdentity.by_name('Red'))
        self.assertEqual(ColorIdentity.R, ColorIdentity.by_name('MonoRed'))
        self.assertEqual(ColorIdentity.R, ColorIdentity.by_name('Embereth'))
        self.assertEqual(ColorIdentity.R, ColorIdentity.by_name('Vulshok'))
        self.assertEqual(ColorIdentity.G, ColorIdentity.by_name('G'))
        self.assertEqual(ColorIdentity.G, ColorIdentity.by_name('Green'))
        self.assertEqual(ColorIdentity.G, ColorIdentity.by_name('MonoGreen'))
        self.assertEqual(ColorIdentity.G, ColorIdentity.by_name('Garenbrig'))
        self.assertEqual(ColorIdentity.G, ColorIdentity.by_name('Sylvok'))
        self.assertEqual(ColorIdentity.WU, ColorIdentity.by_name('WU'))
        self.assertEqual(ColorIdentity.WU, ColorIdentity.by_name('Azorius'))
        self.assertEqual(ColorIdentity.WU, ColorIdentity.by_name('Ojutai'))
        self.assertEqual(ColorIdentity.WB, ColorIdentity.by_name('WB'))
        self.assertEqual(ColorIdentity.WB, ColorIdentity.by_name('Orzhov'))
        self.assertEqual(ColorIdentity.WB, ColorIdentity.by_name('Silverquill'))
        self.assertEqual(ColorIdentity.WR, ColorIdentity.by_name('WR'))
        self.assertEqual(ColorIdentity.WR, ColorIdentity.by_name('Boros'))
        self.assertEqual(ColorIdentity.WR, ColorIdentity.by_name('Lorehold'))
        self.assertEqual(ColorIdentity.WG, ColorIdentity.by_name('WG'))
        self.assertEqual(ColorIdentity.WG, ColorIdentity.by_name('Selesnya'))
        self.assertEqual(ColorIdentity.WG, ColorIdentity.by_name('Dromoka'))
        self.assertEqual(ColorIdentity.UB, ColorIdentity.by_name('UB'))
        self.assertEqual(ColorIdentity.UB, ColorIdentity.by_name('Dimir'))
        self.assertEqual(ColorIdentity.UB, ColorIdentity.by_name('Silumgar'))
        self.assertEqual(ColorIdentity.UR, ColorIdentity.by_name('UR'))
        self.assertEqual(ColorIdentity.UR, ColorIdentity.by_name('Izzet'))
        self.assertEqual(ColorIdentity.UR, ColorIdentity.by_name('Prismari'))
        self.assertEqual(ColorIdentity.UG, ColorIdentity.by_name('UG'))
        self.assertEqual(ColorIdentity.UG, ColorIdentity.by_name('Simic'))
        self.assertEqual(ColorIdentity.UG, ColorIdentity.by_name('Quandrix'))
        self.assertEqual(ColorIdentity.BR, ColorIdentity.by_name('BR'))
        self.assertEqual(ColorIdentity.BR, ColorIdentity.by_name('Rakdos'))
        self.assertEqual(ColorIdentity.BR, ColorIdentity.by_name('Kolaghan'))
        self.assertEqual(ColorIdentity.BG, ColorIdentity.by_name('BG'))
        self.assertEqual(ColorIdentity.BG, ColorIdentity.by_name('Golgari'))
        self.assertEqual(ColorIdentity.BG, ColorIdentity.by_name('Witherbloom'))
        self.assertEqual(ColorIdentity.RG, ColorIdentity.by_name('RG'))
        self.assertEqual(ColorIdentity.RG, ColorIdentity.by_name('Gruul'))
        self.assertEqual(ColorIdentity.RG, ColorIdentity.by_name('Atarka'))
        self.assertEqual(ColorIdentity.WUB, ColorIdentity.by_name('WUB'))
        self.assertEqual(ColorIdentity.WUB, ColorIdentity.by_name('Esper'))
        self.assertEqual(ColorIdentity.WUB, ColorIdentity.by_name('Obscura'))
        self.assertEqual(ColorIdentity.WUR, ColorIdentity.by_name('WUR'))
        self.assertEqual(ColorIdentity.WUR, ColorIdentity.by_name('Jeskai'))
        self.assertEqual(ColorIdentity.WUR, ColorIdentity.by_name('Raugrin'))
        self.assertEqual(ColorIdentity.WUR, ColorIdentity.by_name('Numot'))
        self.assertEqual(ColorIdentity.WUR, ColorIdentity.by_name('Raka'))
        self.assertEqual(ColorIdentity.WUG, ColorIdentity.by_name('WUG'))
        self.assertEqual(ColorIdentity.WUG, ColorIdentity.by_name('Bant'))
        self.assertEqual(ColorIdentity.WUG, ColorIdentity.by_name('Brokers'))
        self.assertEqual(ColorIdentity.WBR, ColorIdentity.by_name('WBR'))
        self.assertEqual(ColorIdentity.WBR, ColorIdentity.by_name('Mardu'))
        self.assertEqual(ColorIdentity.WBR, ColorIdentity.by_name('Savai'))
        self.assertEqual(ColorIdentity.WBR, ColorIdentity.by_name('Oros'))
        self.assertEqual(ColorIdentity.WBR, ColorIdentity.by_name('Dega'))
        self.assertEqual(ColorIdentity.WBG, ColorIdentity.by_name('WBG'))
        self.assertEqual(ColorIdentity.WBG, ColorIdentity.by_name('Abzan'))
        self.assertEqual(ColorIdentity.WBG, ColorIdentity.by_name('Indatha'))
        self.assertEqual(ColorIdentity.WBG, ColorIdentity.by_name('Teneb'))
        self.assertEqual(ColorIdentity.WBG, ColorIdentity.by_name('Necra'))
        self.assertEqual(ColorIdentity.WRG, ColorIdentity.by_name('WRG'))
        self.assertEqual(ColorIdentity.WRG, ColorIdentity.by_name('Naya'))
        self.assertEqual(ColorIdentity.WRG, ColorIdentity.by_name('Cabaretti'))
        self.assertEqual(ColorIdentity.UBR, ColorIdentity.by_name('UBR'))
        self.assertEqual(ColorIdentity.UBR, ColorIdentity.by_name('Grixis'))
        self.assertEqual(ColorIdentity.UBR, ColorIdentity.by_name('Maestros'))
        self.assertEqual(ColorIdentity.UBG, ColorIdentity.by_name('UBG'))
        self.assertEqual(ColorIdentity.UBG, ColorIdentity.by_name('Sultai'))
        self.assertEqual(ColorIdentity.UBG, ColorIdentity.by_name('Zagoth'))
        self.assertEqual(ColorIdentity.UBG, ColorIdentity.by_name('Vorosh'))
        self.assertEqual(ColorIdentity.UBG, ColorIdentity.by_name('Ana'))
        self.assertEqual(ColorIdentity.URG, ColorIdentity.by_name('URG'))
        self.assertEqual(ColorIdentity.URG, ColorIdentity.by_name('Temur'))
        self.assertEqual(ColorIdentity.URG, ColorIdentity.by_name('Ketria'))
        self.assertEqual(ColorIdentity.URG, ColorIdentity.by_name('Intet'))
        self.assertEqual(ColorIdentity.URG, ColorIdentity.by_name('Ceta'))
        self.assertEqual(ColorIdentity.BRG, ColorIdentity.by_name('BRG'))
        self.assertEqual(ColorIdentity.BRG, ColorIdentity.by_name('Jund'))
        self.assertEqual(ColorIdentity.BRG, ColorIdentity.by_name('Riveteers'))
        self.assertEqual(ColorIdentity.WUBR, ColorIdentity.by_name('WUBR'))
        self.assertEqual(ColorIdentity.WUBR, ColorIdentity.by_name('Yore'))
        self.assertEqual(ColorIdentity.WUBR, ColorIdentity.by_name('Artifice'))
        self.assertEqual(ColorIdentity.WUBR, ColorIdentity.by_name('NonG'))
        self.assertEqual(ColorIdentity.WUBG, ColorIdentity.by_name('WUBG'))
        self.assertEqual(ColorIdentity.WUBG, ColorIdentity.by_name('Witch'))
        self.assertEqual(ColorIdentity.WUBG, ColorIdentity.by_name('Growth'))
        self.assertEqual(ColorIdentity.WUBG, ColorIdentity.by_name('NonR'))
        self.assertEqual(ColorIdentity.WURG, ColorIdentity.by_name('WURG'))
        self.assertEqual(ColorIdentity.WURG, ColorIdentity.by_name('Ink'))
        self.assertEqual(ColorIdentity.WURG, ColorIdentity.by_name('Altruism'))
        self.assertEqual(ColorIdentity.WURG, ColorIdentity.by_name('NonB'))
        self.assertEqual(ColorIdentity.WBRG, ColorIdentity.by_name('WBRG'))
        self.assertEqual(ColorIdentity.WBRG, ColorIdentity.by_name('Dune'))
        self.assertEqual(ColorIdentity.WBRG, ColorIdentity.by_name('Aggression'))
        self.assertEqual(ColorIdentity.WBRG, ColorIdentity.by_name('NonU'))
        self.assertEqual(ColorIdentity.UBRG, ColorIdentity.by_name('UBRG'))
        self.assertEqual(ColorIdentity.UBRG, ColorIdentity.by_name('Glint'))
        self.assertEqual(ColorIdentity.UBRG, ColorIdentity.by_name('Chaos'))
        self.assertEqual(ColorIdentity.UBRG, ColorIdentity.by_name('NonW'))
        self.assertEqual(ColorIdentity.WUBRG, ColorIdentity.by_name('WUBRG'))
        self.assertEqual(ColorIdentity.WUBRG, ColorIdentity.by_name('FiveColor'))
        self.assertEqual(ColorIdentity.WUBRG, ColorIdentity.by_name('All'))

    def test_sorting(self):
        ids = [ci for ci in ColorIdentity]
        self.assertListEqual(self.value_order, sorted(ids, key=lambda x: x.value))
        self.assertListEqual(self.wubrg_order, sorted(ids, key=lambda x: x.wubrg_idx))
        self.assertListEqual(self.pentad_order, sorted(ids, key=lambda x: x.pentad_idx))
        self.assertListEqual(self.deck_order, sorted(ids, key=lambda x: x.deck_idx))

    def test_get_color_combinations(self):
        self.assertListEqual(self.wubrg_order, ColorIdentity.get_color_combinations())
        # TODO: Validate this works with various parameters.
