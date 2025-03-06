import tskit

tables = tskit.TableCollection(sequence_length=2)

s0 = tables.nodes.add_row(flags=1, time=0)
s1 = tables.nodes.add_row(flags=1, time=0)
s2 = tables.nodes.add_row(flags=1, time=0)
s3 = tables.nodes.add_row(flags=1, time=0)
s4 = tables.nodes.add_row(flags=1, time=0)
s5 = tables.nodes.add_row(flags=1, time=0)
s6 = tables.nodes.add_row(flags=1, time=0)
s7 = tables.nodes.add_row(flags=1, time=0)
s8 = tables.nodes.add_row(flags=1, time=0)
i0 = tables.nodes.add_row(time=1)
i1 = tables.nodes.add_row(time=2)
i2 = tables.nodes.add_row(time=3)
i3 = tables.nodes.add_row(time=8)
j0 = tables.nodes.add_row(time=10)
j1 = tables.nodes.add_row(time=20)
j2 = tables.nodes.add_row(time=30)
k0 = tables.nodes.add_row(time=15)
k1 = tables.nodes.add_row(time=25)
k2 = tables.nodes.add_row(time=35)
k3 = tables.nodes.add_row(time=37)

tables.edges.add_row(left=0, right=2, parent=k0, child=s4)
tables.edges.add_row(left=0, right=2, parent=k0, child=s5)
tables.edges.add_row(left=0, right=2, parent=k1, child=s6)
tables.edges.add_row(left=0, right=2, parent=k1, child=s7)
tables.edges.add_row(left=0, right=2, parent=k2, child=k0)
tables.edges.add_row(left=0, right=2, parent=k2, child=k1)
tables.edges.add_row(left=0, right=2, parent=k3, child=k2)

tables.edges.add_row(left=0, right=1, parent=i0, child=s0)
tables.edges.add_row(left=0, right=1, parent=i0, child=s1)
tables.edges.add_row(left=0, right=1, parent=i1, child=i0)
tables.edges.add_row(left=0, right=1, parent=i1, child=s2)
tables.edges.add_row(left=0, right=1, parent=i2, child=i1)
tables.edges.add_row(left=0, right=1, parent=i2, child=s3)
tables.edges.add_row(left=0, right=1, parent=i3, child=s8)
tables.edges.add_row(left=0, right=1, parent=i3, child=i2)
tables.edges.add_row(left=0, right=1, parent=k3, child=i3)

tables.edges.add_row(left=1, right=2, parent=j0, child=s0)
tables.edges.add_row(left=1, right=2, parent=j0, child=s1)
tables.edges.add_row(left=1, right=2, parent=j1, child=j0)
tables.edges.add_row(left=1, right=2, parent=j1, child=s2)
tables.edges.add_row(left=1, right=2, parent=j2, child=j1)
tables.edges.add_row(left=1, right=2, parent=j2, child=s3)
tables.edges.add_row(left=1, right=2, parent=k3, child=j2)
tables.edges.add_row(left=1, right=2, parent=k0, child=s8)

tables.sites.add_row(position=0, ancestral_state='A')
tables.sites.add_row(position=1, ancestral_state='A')

tables.mutations.add_row(site=0, node=i2, time=6, derived_state='C')
tables.mutations.add_row(site=1, node=j2, time=32, derived_state='C')

tables.sort()

ts = tables.tree_sequence()

ts.draw_svg("mut_age_and_freq.svg",
            x_axis=False,
            time_scale="time",
            y_label="generations",
            # y_axis=False,
            node_labels={},
            mutation_labels={},
            force_root_branch=True,
)

